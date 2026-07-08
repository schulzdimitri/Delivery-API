from src.main.server.server import app
from src.models.connection.connection import db_connection

if __name__ == "__main__":
    db_connection.connect_to_db()
    app.run(host="0.0.0.0", port=8000, debug=True)
