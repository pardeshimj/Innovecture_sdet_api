import pytest
import requests


@pytest.fixture
def data_fixture():
    _URL = "https://api.coinlore.net/api/tickers/"
    response = requests.get(_URL)
    return response
