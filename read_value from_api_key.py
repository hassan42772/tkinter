import requests
import json
api_key = "ee512e3b141f2b7d550d67dfa50fada9"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "bahawalnagar"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
x = response.json()
print(x)
 


y = x["main"]
current_temperature = y["temp"]
current_pressure = y["pressure"]
current_humidity = y["humidity"]
z = x["weather"]
weather_description = z[0]["description"]

print(current_temperature)
print(current_pressure)
print(current_humidity)
print(weather_description)
print( str(current_temperature)+ "%" +
        "\n atmospheric pressure  = " +
                str(current_pressure) +
        "\n humidity  = " +
                str(current_humidity) +
        "\n description = " +
                str(weather_description))
 
