from flask import Blueprint, jsonify, request
from src.main.http_types.http_request import HttpRequest
from src.main.composer.registry_order_composer import registry_order_composer
from src.main.composer.registry_finder_composer import registry_finder_composer
from src.main.composer.registry_updater_composer import registry_updater_composer

delivery_routes_bp = Blueprint("delivery_routes", __name__)

@delivery_routes_bp.route("/delivery/orders", methods=["POST"])
def registry_order():
    data = request.json
    http_request = HttpRequest(body=data)

    use_case = registry_order_composer()
    response = use_case.registry(http_request)

    return jsonify(response.body), response.status_code

@delivery_routes_bp.route("/delivery/orders/<order_id>", methods=["GET"])
def registry_finder_order(order_id):
    use_case = registry_finder_composer()
    http_request = HttpRequest(path_params={'order_id': order_id})
    response = use_case.find(http_request)

    return jsonify(response.body), response.status_code

@delivery_routes_bp.route("/delivery/orders/<order_id>", methods=["PATCH"])
def registry_updater_order(order_id):
    use_case = registry_updater_composer()
    http_request = HttpRequest(
        path_params={'order_id': order_id},
        body=request.json
    )
    response = use_case.update(http_request)

    return jsonify(response.body), response.status_code