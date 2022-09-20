single_brewery_schema = {
        'type': 'object',
        'properties': {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "brewery_type": {"type": "string"},
                "city": {"type": "string"},
                "postal_code": {"type": "string"},
                "country": {"type": "string"},
                "phone": {"type": "string"},
                "updated_at": {"type": "string"},
                "created_at": {"type": "string"}
        },
        'required': ["id", "name", "brewery_type", "city", "postal_code",
                     "country", "phone", "updated_at", "created_at"]
}
