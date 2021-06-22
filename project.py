import requests

from datetime import datetime

api_key = 'ce3fbf20368ad2b0c8dd098e7f3bc680'
location = input ("Enter the city name: ") 

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

with open('weather.txt','w') as p :

	p.write("-------------------------------------------------------------")
	p.write("\nWeather Stats for - {}  || {}".format(location.upper(), date_time))
	p.write("\n-------------------------------------------------------------")

	p.write("\nCurrent temperature is: {:.2f} deg C".format(temp_city))
	p.write("\nCurrent weather desc  :{}".format(weather_desc))
	p.write("\nCurrent Humidity      :{} %".format(hmdt))
	p.write("\nCurrent wind speed    :{} kmph".format(wind_spd))