import requests
import pytest


@pytest.mark.parametrize('id_res', [3, 5, 10])
def test_create_resources(id_res, url):
    body = {
        'title': 'foo' + str(id_res),
    }
    response = requests.patch(f"{url}/{id_res}", json=body)
    assert response.json().get('title') == body.get('title')
    assert response.json().get('id') == id_res
