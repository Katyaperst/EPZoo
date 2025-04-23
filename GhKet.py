import pytest
import requests

base_url= "https://swagger.rv-school.ru/api/v3/pet"

class TestGhKet:
    def test_add_pet(self):
        budy = {
            "id": 10,
            "name": "doggie",
            "category": {
                "id": 1,
                "name": "Dogs"
            },
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }
        response = requests.post(url=base_url, json=budy)
        assert response.status_code == 200



