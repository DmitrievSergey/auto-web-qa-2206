import pytest
import requests

URL = 'https://dog.ceo/api/breed/'
IMAGE = '/images'


@pytest.mark.parametrize("valid_breed", [
    'affenpinscher',
    "basenji",
    "cattledog"
])
def test_get_image_valid_breed(valid_breed):
    response = requests.get(f"{URL}{valid_breed}{IMAGE}")
    assert response.status_code == 200
    assert response.json().get('status') == 'success'
    assert response.json().get('message')


@pytest.mark.parametrize("not_valid_breed", [
    'affenpinscher1',
    "basenji2",
    "cattledog3"
])
def test_get_image_not_valid_bread(not_valid_breed):
    response = requests.get(f"{URL}{not_valid_breed}{IMAGE}")
    assert response.status_code == 404
    assert response.json().get('status') == 'error'
    assert response.json().get('message') == "Breed not found (master breed does not exist)"
