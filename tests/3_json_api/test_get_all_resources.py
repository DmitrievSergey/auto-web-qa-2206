from jsonschema import validate
import requests

from tests.schemas.json_placeholder import json_schema


def test_get_list(url):
    response = requests.get(f"{url}")
    validate(instance=response.json(), schema=json_schema)
