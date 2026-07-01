from src.models.connection.connection import DBConnection
from src.models.repository.orders import OrdersRepository

db_connection = DBConnection()
db_connection.connect_to_db()
conn = db_connection.get_db_connection()

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_insert_document():
    orders_repository = OrdersRepository(conn)
    my_doc = { "name": "Company Inc", "address": "Highway 37" }
    orders_repository.insert_document(my_doc)

def test_insert_list_of_documents():
    orders_repository = OrdersRepository(conn)
    my_list_of_documents = [
        { "name": "Company Inc", "address": "Highway 37" },
        { "name": "Company Inc", "address": "Highway 36" },
        { "name": "Company Inc", "address": "Highway 35" }
    ]
    orders_repository.insert_list_of_documents(my_list_of_documents)