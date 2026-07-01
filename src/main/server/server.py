from flask import Flask
from src.main.routes.delivery_orders import delivery_routes_bp

app = Flask(__name__)

app.register_blueprint(delivery_routes_bp)