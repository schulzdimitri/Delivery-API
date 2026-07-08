import pytest
from src.models.repository.orders import OrdersRepository

class CollectionMock:
    def __init__(self) -> None:
        self.inserted_document = None
        self.inserted_list = None
        self.find_filter = None
        self.find_one_filter = None
        self.dummy_docs = []

    def insert_one(self, document: dict) -> None:
        self.inserted_document = document
        self.dummy_docs.append(document)

    def insert_many(self, list_of_documents: list[dict]) -> None:
        self.inserted_list = list_of_documents
        self.dummy_docs.extend(list_of_documents)

    def find(self, doc_filter: dict = None) -> list[dict]:
        self.find_filter = doc_filter
        return self.dummy_docs

    def find_one(self, doc_filter: dict = None) -> dict:
        self.find_one_filter = doc_filter
        for doc in self.dummy_docs:
            match = True
            for k, v in doc_filter.items():
                if doc.get(k) != v:
                    match = False
                    break
            if match:
                if "_id" not in doc:
                    doc["_id"] = "mock_id"
                return doc
        return None

class DatabaseMock:
    def __init__(self, collection) -> None:
        self.collection = collection

    def get_collection(self, name: str):
        return self.collection

def test_insert_document():
    collection = CollectionMock()
    conn = DatabaseMock(collection)
    orders_repository = OrdersRepository(conn)
    my_doc = { "name": "Company Inc", "address": "Highway 37" }
    orders_repository.insert_document(my_doc)
    assert collection.inserted_document == my_doc

def test_insert_list_of_documents():
    collection = CollectionMock()
    conn = DatabaseMock(collection)
    orders_repository = OrdersRepository(conn)
    my_list_of_documents = [
        { "name": "Company Inc", "address": "Highway 37" },
        { "name": "Company Inc", "address": "Highway 36" },
        { "name": "Company Inc", "address": "Highway 35" }
    ]
    orders_repository.insert_list_of_documents(my_list_of_documents)
    assert collection.inserted_list == my_list_of_documents

def test_select_many():
    collection = CollectionMock()
    conn = DatabaseMock(collection)
    orders_repository = OrdersRepository(conn)
    
    collection.dummy_docs = [{"cupom": True, "name": "Order 1"}]
    
    doc_filter = { "cupom": True }
    result = orders_repository.select_many(doc_filter)
    
    assert collection.find_filter == doc_filter
    assert len(result) == 1
    assert result[0]["name"] == "Order 1"

def test_select_one():
    collection = CollectionMock()
    conn = DatabaseMock(collection)
    orders_repository = OrdersRepository(conn)
    
    mock_doc = { "name": "Company Inc", "address": "Highway 37", "cupom": True }
    orders_repository.insert_document(mock_doc)

    doc_filter = { "cupom": True }
    result = orders_repository.select_one(doc_filter)
    
    assert result is not None
    assert result["name"] == "Company Inc"
    assert result["address"] == "Highway 37"
    assert result["cupom"] is True
    assert "_id" in result
