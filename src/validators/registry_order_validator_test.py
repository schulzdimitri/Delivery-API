import pytest
from src.validators.registry_order_validator import registry_order_validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError

def test_registry_order_validator():
    body = {
        'data': {
            'name': "Company Inc",
            'address': "Highway 37",
            'cupom': False,
            'items': [
                {'item': "Product 1", 'quantity': 1},
                {'item': "Product 2", 'quantity': 2}
            ]
        }
    }
    
    registry_order_validator(body)

def test_registry_order_validator_with_errors():
    body_with_error = {
        'data': {
            'name': "Company Inc",
            'address': "Highway 37",
            'cupom': "error",
            'items': [
                {'item': "Product 1", 'quantity': 1},
                {'item': "Product 2", 'quantity': 2}
            ]
        }
    }
    
    with pytest.raises(HttpUnprocessableEntityError):
        registry_order_validator(body_with_error)

