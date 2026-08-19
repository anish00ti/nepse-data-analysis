import snowflake.connector
import os
import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env into os.environ




user = os.getenv("SNOWFLAKE_USER")
account = os.getenv("SNOWFLAKE_ACCOUNT")

print(f"Connecting as User: {user} on Account: {account}")
# Do NOT print your password!

def get_snowflake_connection():
    """
    Create and return a Snowflake connection.
    """

    conn = snowflake.connector.connect(
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE", "NEPSE_DATA"),
        database=os.getenv("SNOWFLAKE_DATABASE", "NEPSE_DB"),
        schema=os.getenv("SNOWFLAKE_SCHEMA", "NEPSE_SCHEMA"),
    )

    return conn


if __name__ == "__main__":

    try:
        conn = get_snowflake_connection()

        print("Successfully connected to Snowflake!")

        cursor = conn.cursor()

        cursor.execute("SELECT CURRENT_VERSION()")

        result = cursor.fetchone()

        print("Snowflake Version:", result[0])

        cursor.close()
        conn.close()

        print("Connection closed.")

    except Exception as e:
        print("Snowflake connection failed:")
        print(e)
