from cerberus import Validator

def registry_order_validator(body: dict) -> None:
    body_validator = Validator({
        'data': {
            'type': 'dict',
            'required': True,
            'schema': {
                'name': {'type': 'string', 'required': True},
                'address': {'type': 'string', 'required': True},
                'cupom': {'type': 'boolean', 'required': False},
                'items': {
                    'type': 'list',
                    'schema': {
                        'type': 'dict',
                        'required': True,
                        'schema': {
                            'item': {'type': 'string', 'required': True},
                            'quantity': {'type': 'integer', 'required': True}
                        }
                    }
                }
            }
        }
    })
    
    response = body_validator.validate(body)
    
    if not response:
        raise ValueError(body_validator.errors)
    
    