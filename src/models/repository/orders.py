from src.models.connection.connection import DBConnection
from .interfaces.orders import OrdersRepositoryInterface
from bson.objectid import ObjectId

class OrdersRepository(OrdersRepositoryInterface):
    def __init__(self, db_connection: DBConnection) -> None:
        self.__collection_name = "orders"
        self.__db_connection = db_connection
        
    def insert_document(self, document: dict) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)

    def insert_list_of_documents(self, list_of_documents: list[dict]) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)
    
    def select_many(self, doc_filter: dict = None) -> list[dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(doc_filter)
        return data

    def select_one(self, doc_filter: dict = None) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find_one(doc_filter)
        return data
    
    def select_many_with_properties(self, doc_filter: dict) -> list[dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(
            doc_filter,
            {
                "_id": 0,
                "cupom": 1,
            }
        )
        return data
    
    def select_if_property_exists(self, property_name: str) -> list[dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(
            {"address": {"$exists": True}},
            {"_id": 0, "items": 0}
        )
        return data

    def select_by_object_id(self, object_id: str) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find_one({ "_id": ObjectId(object_id) })
        return data

    def edit_registry(self, object_id: str, new_values: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            { "_id": ObjectId(object_id) },
            { "$set": new_values }
        )
    
    def edit_many_registries(self, doc_filter: dict, new_values: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_many(
            doc_filter,
            { "$set": new_values }
        )

    def edit_registry_with_increment(self, object_id: str, new_values: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            { "_id": ObjectId(object_id) },
            { "$inc": new_values }
        )
    
    def delete_registry(self, object_id: str) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_one({ "_id": ObjectId(object_id) })
    
    def delete_many_registries(self, doc_filter: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_many(doc_filter)
    