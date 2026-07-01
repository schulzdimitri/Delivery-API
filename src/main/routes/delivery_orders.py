from flask import Blueprint

delivery_routes_bp = Blueprint("delivery_routes", __name__)

@delivery_routes_bp.route("/delivery/orders", methods=["POST"])
def registry_order():
    data = request.json
    http_request = HttpRequest(body=data)
    return jsonify({ "message": "Order registered", "data": data }), 201
