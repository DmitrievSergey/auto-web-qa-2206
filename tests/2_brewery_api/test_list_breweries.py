import pytest
import requests
from jsonschema import validate

from tests.schemas.brewery import brewery_schema

URL = 'https://api.openbrewerydb.org/breweries'
BY_PAGE = '?per_page='
BY_CITY = '&by_city='


@pytest.mark.parametrize("page_count", [
    3,
    5,
    10
])
def test_get_list(page_count):
    response = requests.get(f"{URL}{BY_PAGE}{page_count}")
    validate(instance=response.json(), schema=brewery_schema)


@pytest.mark.parametrize("city", [
    'san_diego'
])
def test_get_list_by_city(city, page_count=3):
    response = requests.get(f"{URL}{BY_PAGE}{page_count}{BY_CITY}{city}")


@pytest.mark.parametrize("not_exist_city", [
    'san_diego1'
])
def test_get_list_by_not_exist_city(not_exist_city, page_count=3):
    response = requests.get(f"{URL}{BY_PAGE}{page_count}{BY_CITY}{not_exist_city}")
    assert response.content.__len__() == 2
