from src.models.repository.orders import OrdersRepository
from src.use_cases.registry_order import RegistryOrder
from src.models.connection.connection import db_connection

def registry_order_composer():
    conn = db_connection.get_db_connection()
    model = OrdersRepository(conn)
    use_case = RegistryOrder(model)
    
    return use_case