import io
import matplotlib.pyplot as plt
import logging
from fastapi import APIRouter, Body
from llm import OpenAIChatbot
from manage_db import exec_sql_query
from utils import preprocess_code
from config import CONTEXT, VISUALIZATION_PROMPT


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
    logger.info("Received request to generate SQL")
    logger.info(f"Message: {message}")
    logger.info(f"History: {history}")

    # Combine initial context (database description) and history
    assert isinstance(history, list)

    history = [{"role": "system", "content": context}] + [
        {"role": "user", "content": message} for message in history
    ]

    # Generate SQL query
    chatbot = OpenAIChatbot()
    sql_response = chatbot.chat(message=message, history=history)
    sql_response = preprocess_code(sql_response)

    # Log query and response
    logger.info(f"Initial context: {context}")
    logger.info(f"History: {history}")
    logger.info(f"Generated SQL: {sql_response}")

    # Execute SQL query on database
    data = exec_sql_query(sql_query=sql_response)

    # Generate visualization code
    history = history + [{"role": "system", "content": sql_response}]
    vis_response = chatbot.chat(message=VISUALIZATION_PROMPT, history=history)
    vis_response = preprocess_code(vis_response)

    # Log visualization code
    logger.info(f"Generated visualization code: {vis_response}")

    # Execute visualization code
    buf = io.BytesIO()
    exec(vis_response)
    image = buf.getvalue()
    plt.show()

    # Return SQL query result and visualization plot
    return {
        "sql_response": sql_response,
        "vis_response": vis_response,
        "data": data,
        "image": image,
    }