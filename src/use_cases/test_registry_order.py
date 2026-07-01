from src.main.http_types.http_request import HttpRequest
from src.use_cases.registry_order import RegistryOrder

class OrderRepositoryMock:
    def __init__(self) -> None:
        self.insert_document_att = {}

    def insert_document(self, document: dict) -> None:
        self.insert_document_att["document"] = document

class OrderRepositoryMockError:
    def insert_document(self, document: dict) -> None:
        raise Exception("Error on insert document")

def test_registry_order():
    repo = OrderRepositoryMock()
    registry_order = RegistryOrder(repo)

    order_data = {
        "name": "João",
        "address": "Rua A, 123",
        "cupom": False,
        "items": [
            {"item": "Chocolate", "quantidade": 2}, 
            {"item": "Refrigerante", "quantidade": 1}
        ]
    }

    http_request = HttpRequest(
        body={"data": order_data}
    )
    response = registry_order.registry(http_request)

    assert response.status_code == 201
    assert response.body == {
        "data": {
            "type": "Order",
            "count": 1,
            "registry": True
        }
    }

def test_registry_order_error():
    repo = OrderRepositoryMockError()
    registry_order = RegistryOrder(repo)
    
    http_request = HttpRequest(body={})
    response = registry_order.registry(http_request)
    assert response.status_code == 400
    assert "error" in response.body
