import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    TOKEN = os.environ.get('TOKEN')
    URL = os.environ.get('URL')
    DATA_JSON = os.environ.get('DATA_JSON')
    USER = os.environ.get('USER')
    PASSWORD = os.environ.get('PASSWORD')
    DB_NAME = os.environ.get('DB_NAME')
    HOST = os.environ.get('HOST')
