from dotenv import load_dotenv
from pathlib import Path
import os
import pyodbc

BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / ".env"

load_dotenv(dotenv_path=env_path)

SERVER = os.getenv("SQL_SERVER")
USERNAME = os.getenv("SQL_USERNAME")
AUTH_MODE = os.getenv("AUTH_MODE", "ActiveDirectoryInteractive")


def get_conn(database: str):

    conn_parts = [
        "Driver={ODBC Driver 18 for SQL Server}",
        f"Server=tcp:{SERVER},1433",
        f"Database={database}",
        f"Authentication={AUTH_MODE}",
        "Encrypt=yes",
        "TrustServerCertificate=no",
    ]

    if USERNAME:
        conn_parts.append(f"UID={USERNAME}")

    conn_str = ";".join(conn_parts) + ";"

    return pyodbc.connect(conn_str)