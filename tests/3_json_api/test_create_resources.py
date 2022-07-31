import requests


def test_create_resources(url):
    body = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1,
    }
    response = requests.post(url, json=body)
    assert response.json().get('userId') == body.get('userId')
    assert response.json().get('title') == body.get('title')
    assert response.json().get('body') == body.get('body')
