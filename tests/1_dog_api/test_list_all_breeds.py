import requests
from jsonschema import validate

from tests.schemas.dog_list import valid_schema

URL = 'https://dog.ceo/api/breeds/list/all'


def test_list():
    response = requests.get(URL)
    assert response.status_code == 200
    assert response.json().get('status') == 'success'
    validate(instance=response.json(), schema=valid_schema)
