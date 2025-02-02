import io
import matplotlib.pyplot as plt
import logging
import base64
import json
from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from llm import OpenAIChatbot
from manage_db import exec_sql_query
from utils import preprocess_code
from config import (
    INTENT_CLASSIFICATION_PROMPT,
    CONTEXT,
    GENERAL_CHAT_RESPONSE,
    get_visualization_prompt,
)


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define API endpoint
router = APIRouter()

@router.post("/query_db")
async def query_db(
    message: str = Body(...),
    history: list[str] = Body(...),
    context: list[str] = CONTEXT,
) -> str:
    """
    Generate SQL from user input using an LLM. Then execute the SQL query on the database.

    Args:
    - message: The latest user input describing the query.
    - history: A list of past interactions for context-aware generation.

    Returns:
    - A SQL query result from the database.
    """
    logger.info("Received request.")
    logger.info(f"Message: {message}")
    logger.info(f"History: {history}")

    # Classify user intent
    chatbot = OpenAIChatbot()
    history_intent_context = get_history(
        context=INTENT_CLASSIFICATION_PROMPT, history=history
    )
    intent = chatbot.chat(message=message, history=history_intent_context)
    intent = intent.strip().lower()
    logger.info(f"Intent classification: {intent}")

    if intent == "chat":
        history_chat_context = get_history(
            context=GENERAL_CHAT_RESPONSE, history=history
        )
        response = chatbot.chat(message=message, history=history_chat_context)
        return JSONResponse(
            content={
                "sql_response": response,
                "vis_response": "",
                "data": json.dumps([]),
                "image": [],
            }
        )

    if intent != "database":
        raise ValueError("Invalid intent classification.")

    # Database interaction and visualization intent
    # Generate SQL query
    chatbot = OpenAIChatbot()
    history_db_context = get_history(context=context, history=history)
    sql_response = chatbot.chat(message=message, history=history_db_context)
    sql_response = preprocess_code(sql_response)

    logger.info(f"Initial context: {context}")
    logger.info(f"History: {history}")
    logger.info(f"Generated SQL: {sql_response}")

    # Execute SQL query on database
    data = exec_sql_query(sql_query=sql_response)
    logger.info(f"Executed SQL query: {data}")

    # Generate visualization code
    VISUALIZATION_PROMPT = get_visualization_prompt(data)
    logger.info(f"Visualization prompt: {VISUALIZATION_PROMPT}")

    history_vis = get_history(context=VISUALIZATION_PROMPT, history=sql_response)
    vis_response = chatbot.chat(message='', history=history_vis)
    vis_response = preprocess_code(vis_response)
    logger.info(f"Generated visualization code: {vis_response}")

    # Execute visualization code
    buf = io.BytesIO()
    try:
        exec(
            vis_response, {"plt": plt, "io": io, "buf": buf}
        )  # Execute with safe context
        plt.savefig(buf, format="png")  # Save figure to buffer
        plt.close()
        buf.seek(0)
        image_base64 = base64.b64encode(buf.getvalue()).decode(
            "utf-8"
        )  # Convert to base64
    except Exception as e:
        logger.error(f"Error executing visualization code: {e}")
        image_base64 = None
    # plt.show()

    # Return SQL query result and visualization plot
    return JSONResponse(
        content={
            "sql_response": sql_response,
            "vis_response": vis_response,
            "data": json.dumps(data),  # Convert list to JSON string
            "image": image_base64,
        }
    )


def get_history(context: str, history: list[str]) -> list[dict]:
    """Creates a history of interactions with the AI model, taking into account the original purpose of the conversation."""
    history = [{"role": "system", "content": context}] + [
        {"role": "user", "content": message} for message in history
    ]
    return history
