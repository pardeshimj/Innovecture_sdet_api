import pytest


def check_api_status(resp_data):
    """
    :param resp_data:
    :return:
    """
    status_code = resp_data.status_code
    if status_code == '200':
        return True
    return False


def test_check_btc_price(data_fixture):
    if check_api_status(data_fixture):
        for i in data_fixture['data']:
            if i['symbol'] == "BTC":
                assert float(i['price_usd']) > float(30000.0), \
                    f"The price of BTC is {i['price_usd']} with less than $30000"


def test_check_eth_price(data_fixture):
    if check_api_status(data_fixture):
        for i in data_fixture['data']:
            if i['symbol'] == "ETH":
                assert float(i['price_usd']) > float(15000.0), \
                    f"The price of BTC is {i['price_usd']} with less than $15000"
