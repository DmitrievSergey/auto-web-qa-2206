import requests
from jsonschema import validate

URL = 'https://dog.ceo/api/breeds/image/random'


def test_get_image_valid_breed():
    response = requests.get(URL)
    assert response.status_code == 200
    assert response.json().get('status') == 'success'
    assert response.json().get('message')
