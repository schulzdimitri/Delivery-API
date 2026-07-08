# Delivery Order Management API


A Python-based backend service designed to manage delivery orders. Built with Flask, MongoDB (via PyMongo), and Cerberus for robust data validation, this application follows clean architecture principles (Separation of Concerns, Repository Pattern, and Dependency Injection/Composers).

![Python](https://img.shields.io/badge/python-3.13+-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
![Cerberus](https://img.shields.io/badge/Cerberus-orange?style=for-the-badge)
![Pytest](https://img.shields.io/badge/pytest-%230A9EDC.svg?style=for-the-badge&logo=pytest&logoColor=white)
![Dotenv](https://img.shields.io/badge/dotenv-black?style=for-the-badge)

---

## 📁 Architecture & Directory Structure

The project is structured as follows:

```shell
├── conftest.py                                 # Pytest configuration file
├── requirements.txt                            # Project dependencies
├── run.py                                      # Application entry point
├── src
│   ├── errors                                  # Custom HTTP Exception Types and Centralized Error Handler
│   │   ├── error_handler.py
│   │   └── types
│   │       ├── http_not_found.py
│   │       └── http_unprocessable_entity.py
│   ├── main
│   │   ├── composer
│   │   │   ├── registry_finder_composer.py
│   │   │   ├── registry_order_composer.py
│   │   │   └── registry_updater_composer.py
│   │   ├── http_types
│   │   │   ├── http_request.py
│   │   │   └── http_response.py
│   │   ├── routes
│   │   │   └── delivery_orders.py
│   │   └── server
│   │       └── server.py
│   ├── models
│   │   ├── connection
│   │   │   └── connection.py
│   │   └── repository
│   │       ├── orders.py
│   │       └── orders_test.py
│   ├── use_cases                                # Application business logic
│   │   ├── registry_finder.py
│   │   ├── registry_order.py
│   │   └── registry_updater.py
│   └── validators                               # Data validation schemas using Cerberus
│       ├── registry_order_validator.py
│       └── registry_updater_validator.py
```

---

## ⚙️ Configuration & Environment Setup

1. **Clone the Repository** and navigate to the project directory.

2. **Create a Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**:
   Create a `.env` file in the root directory with the following variables:
   ```env
   DB_USER=admin
   DB_PASSWORD=password
   DB_HOST=localhost
   DB_PORT=27017
   DB_NAME=rocket_db
   ```

---

## 🖥️ Running the Application

Ensure MongoDB is running locally (defaulting to the credentials defined in `.env`), then start the Flask application:

```bash
python run.py
```

The server will be available at `http://localhost:8000`.

---

## 📡 API Endpoints

### 1. Register a New Order
* **Endpoint**: `POST /delivery/orders`
* **Content-Type**: `application/json`
* **Request Body Schema**:
  ```json
  {
    "data": {
      "name": "João",
      "address": "Rua A, 123",
      "cupom": false,
      "items": [
        {
          "item": "Chocolate",
          "quantity": 2
        }
      ]
    }
  }
  ```
* **Success Response (201 Created)**:
  ```json
  {
    "data": {
      "type": "Order",
      "count": 1,
      "registry": true
    }
  }
  ```

---

### 2. Find an Order by ID
* **Endpoint**: `GET /delivery/orders/<order_id>`
* **Success Response (200 OK)**:
  ```json
  {
    "data": {
      "count": 1,
      "type": "order",
      "attributes": {
        "_id": "603d758df...",
        "name": "João",
        "address": "Rua A, 123",
        "cupom": false,
        "items": [
          {
            "item": "Chocolate",
            "quantity": 2
          }
        ],
        "created_at": "2026-07-08T02:00:00"
      }
    }
  }
  ```

---

### 3. Update an Order
* **Endpoint**: `PATCH /delivery/orders/<order_id>`
* **Content-Type**: `application/json`
* **Request Body Schema**:
  ```json
  {
    "data": {
      "name": "João Updated",
      "address": "Rua B, 456",
      "cupom": true
    }
  }
  ```
* **Success Response (200 OK)**:
  ```json
  {
    "data": {
      "order_id": "603d758df...",
      "type": "order",
      "count": 1
    }
  }
  ```

---

## 🧪 Testing

To run the automated tests (unit tests for repositories, use cases, validators, and endpoints using manual mocks):

```bash
pytest
```
