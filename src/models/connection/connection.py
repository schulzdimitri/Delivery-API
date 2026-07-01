from pymongo import MongoClient
from dotenv import load_dotenv
import os

class DBConnection:
    def __init__(self) -> None:
        load_dotenv()
        self.__connection_string = f"mongodb://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@${os.getenv('DB_HOST')}:${os.getenv('DB_PORT')}/?authSource=admin"
        self.__database_name = os.getenv('DB_NAME')
        self.__client = None
        self.__db_connection = None

    def connect_to_db(self) -> None:
        self.__client = MongoClient(self.__connection_string)
        self.__db_connection = self.__client[self.__database_name]
        
    def get_db_connection(self):
        return self.__db_connection
