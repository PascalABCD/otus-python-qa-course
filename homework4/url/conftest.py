import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="Request url, default parameter https://ya.ru"
    )

    parser.addoption(
        "--status_code",
        default="200",
        choices=["200", "201", "204", "304", "400 ", "401", "403", "404", "500", "501", "502", "503", "504"],
        help="Status code"
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return int(request.config.getoption("--status_code"))
