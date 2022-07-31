import pytest
import requests

URL = 'https://dog.ceo/api/breed/'
IMAGE = '/images'


@pytest.mark.parametrize("valid_breed, valid_subbreed", [
    ('bulldog', 'boston')
])
def test_get_image_valid_breed(valid_breed, valid_subbreed):
    response = requests.get(f"{URL}{valid_breed}/{valid_subbreed}{IMAGE}")
    assert response.status_code == 200
    assert response.json().get('status') == 'success'
    assert response.json().get('message')


@pytest.mark.parametrize("valid_breed, not_valid_subbreed", [
    ('bulldog', 'boston1')
])
def test_get_image_not_valid_bread(valid_breed, not_valid_subbreed):
    response = requests.get(f"{URL}{valid_breed}/{not_valid_subbreed}{IMAGE}")
    assert response.status_code == 404
    assert response.json().get('status') == 'error'
    assert response.json().get('message') == 'Breed not found (sub breed does not exist)'
