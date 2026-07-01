from models.connection.connection import DBConnection

class OrdersRepository:
    def __init__(self, db_connection: DBConnection) -> None:
        self.__collection_name = "orders"
        self.__db_connection = db_connection
        
    def insert_document(self, document: dict) -> dict:
        collection = self.__db_connection.get_collection[self.__collection_name]
        collection.insert_one(document)

    def insert_list_of_documents(self, list_of_documents: list[dict]) -> None:
        collection = self.__db_connection.get_collection[self.__collection_name]
        collection.insert_many(list_of_documents)