from src.models.repository.interfaces.orders import OrdersRepositoryInterface
from src.main.http_types.http_response import HttpResponse
from src.main.http_types.http_request import HttpRequest
from src.errors.types.http_not_found import HttpNotFoundError
from src.errors.error_handler import error_handler

class RegistryFinder:
    def __init__(self, orders_repository: OrdersRepositoryInterface) -> None:
        self.__orders_repository = orders_repository

    def find_all(self, http_request: HttpRequest) -> HttpResponse:
        try:
            order_id = http_request.path_params["order_id"]
            order = self.__search_order(order_id)
            self.__format_response(order)
        except Exception as exception:
            return error_handler(exception)
    
    def __search_order(self, order_id: str) -> dict:
        order = self.__orders_repository.select_by_object_id(order_id)
        if not order: raise HttpNotFoundError("Order not found")
        return order

    def __format_response(self, order: dict) -> dict:
        order["_id"] = str(order["_id"])
        return HttpResponse(
            body={
                "data": {
                    "count": 1,
                    "type": "order",
                    "attributes": order
                }
            },
            status_code=200
        )
    