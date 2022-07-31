import pytest
import requests

URL = 'https://jsonplaceholder.typicode.com/posts/'


@pytest.mark.parametrize("id_resource", [
    3,
    5,
    10
])
def test_get_list(id_resource):
    response = requests.get(f"{URL}{id_resource}")
    assert response.json().get('id') == id_resource
