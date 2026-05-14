from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path("../.env")

load_dotenv(dotenv_path=env_path)

SERVER = os.getenv("SQL_SERVER")

print("ENV PATH:", env_path.resolve())
print("SERVER:", SERVER)