import requests

def weather():
    url= 'http://api.openweathermap.org/data/2.5/weather?appid=b785080d09ffe12ee852f2035e884903&q=Kiev'
    json_content = requests.get(url).json()
    json_content = json_content.pop("weather")
    json_content = json_content.pop()
    current_weather = json_content.pop("main")

    return current_weather

my_weat = weather()
print(my_weat)