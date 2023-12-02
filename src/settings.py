from os import environ

from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST = environ.get("POSTGRES_HOST")
POSTGRES_PORT = environ.get("POSTGRES_PORT")
POSTGRES_DB = environ.get("POSTGRES_DB")
PATH_TO_DB = environ.get("PATH_TO_SQLITE")
