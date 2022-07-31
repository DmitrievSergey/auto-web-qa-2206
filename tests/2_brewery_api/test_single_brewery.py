import pytest
import requests

URL = 'https://api.openbrewerydb.org/breweries/'


@pytest.mark.parametrize("valid_brewery", [
    'circle-9-brewing-san-diego',
    "barrel-brothers-brewing-company-windsor",
    "bay-brewing-company-miami"
])
def test_get_image_valid_breed(valid_brewery):
    response = requests.get(f"{URL}{valid_brewery}")
    assert response.status_code == 200


@pytest.mark.parametrize("not_valid_brewery", [
    'affenpinscher1',
    "basenji2",
    "cattledog3"
])
def test_get_not_valid_bread(not_valid_brewery):
    response = requests.get(f"{URL}{not_valid_brewery}")
    assert response.status_code == 404
    assert response.json().get('status') is None
