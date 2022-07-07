
# Request for getting data 
import requests 

API_KEY = 

# Where I am sending the request to
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

city = input('Enter a city name: ')

# Query parameters. Base URL is passing along API Key (Query Parameter)
request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'

# Send 'get' request because I am trying to request data 
response = requests.get(request_url)

#response should return data 

# a status code request of 200 means that it is sucessful 
if response.status_code == 200:
    data = response.json() #data will be returned as json (python dictionary)
    weather = data['weather'][0]['description']
    print(weather.capitalize())
    temperture = round((data['main']['temp'] - 273.15) * 1.8 + 32) # Formula for converting Kelvin to
    print(f'{temperture} Degrees Fahrenheit')
    if temperture > 80:
        print('Wear shorts and short sleeves!!')
    elif temperture > 60:
        print('The best kind of temperture')
    else:
        print('Dont forget your jacket!!')