import pytest
import requests


@pytest.mark.parametrize("id_resource", [3, 5, 10])
def test_get_list(id_resource, url):
    response = requests.get(f"{url}/{id_resource}")
    assert response.json().get('id') == id_resource
