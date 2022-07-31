import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url", action="store", default='https://jsonplaceholder.typicode.com/posts',
        help="default url",
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")
