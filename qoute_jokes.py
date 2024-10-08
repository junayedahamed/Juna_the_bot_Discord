import requests
import json

import api
def get_qoute():
    responce = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(responce.text)

    qoute = json_data[0]['q'] + " _" + json_data[0]['a']
    print(json_data)
    return (qoute)


def get_jokes():
    limit=3
    app_url='https://api.api-ninjas.com/v1/jokes'.format(limit)
    jokes=requests.get(app_url,headers={'X-Api-Key': api.MY_API})

    if jokes.status_code==requests.codes.ok:
        jokes_d=jokes.text
        # print((()))

        return jokes_d[11:-3]


