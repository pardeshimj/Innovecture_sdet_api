# Innovecture_sdet_api
Create test to check Crypto currency.

### test_api_data.py 
This file contain the validation of BTC and ETH prices bassed on condition which can be run using below pytest command

"pytest test_api_data.py -v -s"

### changed_24_data_json.py
This file contains the code logic to check the last 24 hrs percent change data and
based on that create new "result_24_hr_data.json" file
which can be executed using 

"python changed_24_data_json.py"

#### Note: 
There is requirement.txt which contained the required libraries for this execution

