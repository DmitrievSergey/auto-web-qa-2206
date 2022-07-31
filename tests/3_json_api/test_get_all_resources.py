from jsonschema import validate
import requests

from tests.schemas.json_placeholder import json_schema

URL = 'https://jsonplaceholder.typicode.com/posts'


def test_get_list():
    response = requests.get(f"{URL}")
    validate(instance=response.json(), schema=json_schema)
