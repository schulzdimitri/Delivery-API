from src.models.repository.orders import OrdersRepository
from src.models.connection.connection import db_connection
from src.use_cases.registry_updater import RegistryUpdater

def registry_updater_composer():
    conn = db_connection.get_db_connection()
    model = OrdersRepository(conn)
    use_case = RegistryUpdater(model)
    return use_case