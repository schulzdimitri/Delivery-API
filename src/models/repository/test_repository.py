import pytest
from src.models.repository.orders import OrdersRepository

db_connection = DBConnection()
db_connection.connect_to_db()
conn = db_connection.get_db_connection()

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_insert_document():
    orders_repository = OrdersRepository(conn)
    my_doc = { "name": "Company Inc", "address": "Highway 37" }
    orders_repository.insert_document(my_doc)

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_insert_list_of_documents():
    orders_repository = OrdersRepository(conn)
    my_list_of_documents = [
        { "name": "Company Inc", "address": "Highway 37" },
        { "name": "Company Inc", "address": "Highway 36" },
        { "name": "Company Inc", "address": "Highway 35" }
    ]
    orders_repository.insert_list_of_documents(my_list_of_documents)

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_select_many():
    orders_repository = OrdersRepository(conn)
    doc_filter = { "cupom": True }
    result = orders_repository.select_many(doc_filter)
    
    for doc in result:
        print(doc)

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_select_one():
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
