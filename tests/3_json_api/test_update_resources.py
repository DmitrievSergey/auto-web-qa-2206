import requests
import pytest


@pytest.mark.parametrize('id_res', [3, 5, 10])
def test_create_resources(id_res, url):
    body = {
        'id': id_res,
        'title': 'foo',
        'body': 'bar',
        'userId': 1,
    }
    response = requests.put(f"{url}/{id_res}", json=body)
    assert response.json().get('userId') == body.get('userId')
    assert response.json().get('title') == body.get('title')
    assert response.json().get('body') == body.get('body')
    assert response.json().get('id') == id_res
