import requests

URL = 'https://jsonplaceholder.typicode.com/posts'


def test_create_resources():
    body = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1,
    }
    response = requests.post(URL, json=body)
    assert response.json().get('userId') == body.get('userId')
    assert response.json().get('title') == body.get('title')
    assert response.json().get('body') == body.get('body')
