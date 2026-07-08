from src.models.repository.orders import OrdersRepository
from src.models.connection.connection import db_connection
from src.use_cases.registry_finder import RegistryFinder

def registry_finder_composer():
    conn = db_connection.get_db_connection()
    model = OrdersRepository(conn)
    use_case = RegistryFinder(model)
    return use_case