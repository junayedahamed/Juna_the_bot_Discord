import requests
from configparser import ConfigParser
from weather import country_names
import datetime
def get_weather(city):
    config_file = 'config.ini'
    config = ConfigParser()
    config.read(config_file)
    api_key = config['api_key']['key']
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    try:

        result = requests.get(url.format(city, api_key))

    except:

        print( "No such City")

    if result.status_code==requests.codes.ok:

        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_centigrade = temp_kelvin - 273.15
        temp_farhrenheit = (temp_kelvin - 273.15) * 9 / 5 + 32
        weather = json['weather'][0]['main']
        # condition=icon(weather)
        final = [city, country, temp_farhrenheit, temp_centigrade, weather]
        # print(f"{datetime.time.hour}:{datetime.time.minute}:{datetime.time.second}")
        if final[1]=='IL':
            return "😡😡 Terrorist Country As a bot i will not provide you any kind if info about this country 👊👊"
        else:
            return f'Country name: {country_names.countries_dict[final[1]]}\nCity name: {final[0]}\nTemp in F:{round(final[2],2)}\N{DEGREE SIGN}\nTemp in Celsius: {round(final[3],2)}\N{DEGREE SIGN}\nCondition: {final[4]}\nHave a beautiful day sir 😊😊'
    else:
        return f"No City Found named '{city}'"
