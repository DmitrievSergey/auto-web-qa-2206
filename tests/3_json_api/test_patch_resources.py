import requests
import pytest

URL = 'https://jsonplaceholder.typicode.com/posts/'


@pytest.mark.parametrize('id_res', [
    3,
    5,
    10
])
def test_create_resources(id_res):
    body = {
        'title': 'foo' + str(id_res),
    }
    response = requests.patch(f"{URL}{id_res}", json=body)
    assert response.json().get('title') == body.get('title')
    assert response.json().get('id') == id_res
