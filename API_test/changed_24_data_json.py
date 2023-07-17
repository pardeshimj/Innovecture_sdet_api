import json
import requests


def get_data(site_url: str):
    """
    :param site_url:  The API site URL to get data
    :return:  JSON of API response
    """
    response = requests.get(site_url)
    return response


def create_json_24hr_data(all_data: json):
    """
    :param all_data: The json response data
    :return: Create JSON based on the percentage change in last 24 hrs (should be > 1%)
    """
    result_dict = list()
    try:
        for data in all_data['data']:
            if abs(float(data['percent_change_24h'])) > 1:
                result_dict.append(data)
        with open('result_24_hr_data.json', 'w', encoding='utf-8') as output_json:
            json.dump(result_dict, output_json, indent=4)
    except Exception as e:
        print("The creation failed with ", e)


_URL = "https://api.coinlore.net/api/tickes/"
resp_data = get_data(_URL)
if resp_data.status_code == 200:
    create_json_24hr_data(resp_data.json())
else:
    print("Failed with error status code ", resp_data.status_code)
