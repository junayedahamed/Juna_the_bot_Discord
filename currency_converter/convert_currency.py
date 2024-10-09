import requests
import api
def converter(amount,fCurrency,lcurrency):
    api_url = f'https://api.api-ninjas.com/v1/convertcurrency?have={fCurrency}&want={lcurrency}&amount={amount}'
    response = requests.get(api_url, headers={'X-Api-Key': api.MY_API})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        return "This feature is currently unavilable"