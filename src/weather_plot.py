import json
from pprint import pprint
import requests
import matplotlib.pyplot as plt

app_id = 'Xe4SqYMtagz4ZGW4HUwj'
app_code = 'Oq2RudhmsvvkhJv5ZIgZdQ'

url = 'https://weather.api.here.com/weather/1.0/report.json?app_id={}&app_code={}&product=forecast_7days_simple&name=Boston'.format(app_id,app_code)

def plot_weather():
	response = requests.get(url)
	weather_json = json.loads(response.text)

	data = weather_json['dailyForecasts']['forecastLocation']['forecast']
	high_temp = []
	low_temp = []
	humidity = []
	precipitation_probability = []
	days = []
	plt.title('Variation for the week')
	for day in data:
		# print('Day : ', str(day['dayOfWeek'])) 	# str(day['weekday']))
		# print('High Temp : ',str(day['highTemperature']))
		# print('Low Temp : ',str(day['lowTemperature']))
		# print('Humidity : ',str(day['humidity']))
		# print('Rainfall Prob : ',str(day['precipitationProbability']))
		days.append(day['weekday'])
		high_temp.append(day['highTemperature'])
		low_temp.append(day['lowTemperature'])
		humidity.append(day['humidity'])
		precipitation_probability.append(day['precipitationProbability'])
		# plt.plot(int(day['dayOfWeek']),float(day['highTemperature']),int(day['dayOfWeek']),float(day['lowTemperature']),int(day['dayOfWeek']),float(day['humidity']),int(day['dayOfWeek']),float(day['precipitationProbability']))
		# plt.plot(int(day['dayOfWeek']),float(day['highTemperature']),'r')
		# plt.plot(int(day['dayOfWeek']),float(day['lowTemperature']),'g')
		# plt.plot(int(day['dayOfWeek']),float(day['humidity']),'b')
		# plt.plot(int(day['dayOfWeek']),float(day['precipitationProbability']))
		# plt.pause(0.0001)

	plt.xticks(high_temp,days)
	plt.scatter(days, high_temp, days, low_temp, days, humidity, days, precipitation_probability)
	plt.legend(loc='upper right')
	plt.show()