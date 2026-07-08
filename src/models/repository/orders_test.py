from src.models.repository.orders import OrdersRepository

class CollectionMock():
    def __init__(self) -> None:
        self.insert_one_attributes = {}
        self.find_attributes = {}

    def insert_one(self, data: any) -> None:
        self.insert_one_attributes["dict"] = data

    def find(self, *args) -> None:
        self.find_attributes["args"] = args
    
class DBCollectionMock():
    def __init__(self, collection: str) -> None:
        self.get_collection_attributes = {}
        self.__collection = collection
    
    def get_collection(self, collection_name: str):
        self.get_collection_attributes["name"] = collection_name
        return self.__collection

def test_insert_document():
    collection = CollectionMock()
    db_connection = DBCollectionMock(collection)
    repository = OrdersRepository(db_connection)

    doc = { "something": "data" }

    repository.insert_document(doc)

    assert collection.insert_one_attributes["dict"] == doc
    