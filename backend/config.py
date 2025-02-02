# Webapp configuration settings
HOST: str = "127.0.0.1"
PORT: int = 8000

# OpenAI API configuration
LLM_MODEL: str = "gpt-4o-mini"
MAX_RETRIES: int = 3
RETRY_DELAY: int = 2

# Fixed prompts for the AI model

with open('backend/database_file/schema.txt', 'r') as f:
    SCHEMA = f.read()

CONTEXT: str = f"""
    CONTEXT: You are an AI that converts user text into SQL queries. Users input natural language questions or requests, and you generate the corresponding SQL query to retrieve and/or manipulate data.

    SCHEMA DESCRIPTION: The schema of the database contains the following data:
    {SCHEMA}.
    The table is called 'people'.

    ANSWER: Provide simple SQL query that corresponds to the user's request. Only provide the SQL query to retrieve the relevant data, not to analyze or process it.

    RESPONSE CONSTRAINT: DO NOT OUTPUT HISTORY OF CHAT, JUST OUTPUT THE SQL QUERY.
"""

def get_visualization_prompt(data):
    VISUALIZATION_PROMPT: str = f"""
        CONTEXT: You are now an AI that generates visualizations for data analysis. Given the previous SQL query, you need to generate code for a visualization that represents the data in a meaningful way.
        Assume the actual result of the previous SQL query is stored in a variable called `data`.
        Here's the content of the `data` variable:
        {data}.
        \n\n

        You need to convert it into numpy arrays or pandas dataframes than use matplotlib to generate the visualization. Assume these libraries are available for use.

        ANSWER: Generate code for data conversion and visualization based on the SQL query result. Dont include plt.show() or any other display functions.

        RESPONSE CONSTRAINT: DO NOT OUTPUT HISTORY OF CHAT, JUST OUTPUT THE VISUALIZATION CODE, ONLY PYTHON CODE.
    """
    return VISUALIZATION_PROMPT