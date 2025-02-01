import os
import sqlite3


def exec_sql_query(sql_query: str) -> str:
    """
    Execute a SQL query on the database.

    Args:
    - sql_query: The SQL query to execute.

    Returns:
    - The result of the SQL query.
    """
    # Connect to database
    conn = sqlite3.connect(os.path.join('backend', 'database_file', 'dummy.db'))
    cursor = conn.cursor()

    # Execute SQL query
    cursor.execute(sql_query)
    result = cursor.fetchall()

    # Close database connection
    conn.close()

    return result