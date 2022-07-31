
import requests


def test_module(url, status_code):
    response = requests.get(url)
    assert response.status_code == int(status_code)



