import logging
from fastapi import APIRouter, Form
from llm import OpenAIChatbot
from config import CONTEXT


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define API endpoint
router = APIRouter()

@router.post("/query_db")
async def query_db(
    message: str = Form(...),
    history: list[str] = Form(...),
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
    response = chatbot.chat(message=message, history=history)

    # Log query and response
    logger.info(f"Initial context: {context}")
    logger.info(f"History: {history}")
    logger.info(f"Generated SQL: {response}")

    # Execute SQL query on database
    # ...

    return response