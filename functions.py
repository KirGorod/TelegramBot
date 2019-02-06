import requests
import random

#data_string = {'coord': {'lon': 30.52, 'lat': 50.43}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'base': 'stations', 'main': {'temp': 273.15, 'pressure': 1028, 'humidity': 92, 'temp_min': 273.15, 'temp_max': 273.15}, 'visibility': 10000, 'wind': {'speed': 1, 'deg': 100}, 'clouds': {'all': 90}, 'dt': 1549395000, 'sys': {'type': 1, 'id': 8898, 'message': 0.0036, 'country': 'UA', 'sunrise': 1549344362, 'sunset': 1549378713}, 'id': 703448, 'name': 'Kiev', 'cod': 200}

def take_data(City="Kiev"):
    data = get_weather(City)

    return data

def get_weather(City="Kiev"):
    url = f'http://api.openweathermap.org/data/2.5/weather?appid=b785080d09ffe12ee852f2035e884903&q={City}'
    data = requests.get(url).json()
    json_content = data

    if "message" not in json_content:
        json_content = json_content.pop("weather")
        json_content = json_content.pop()
        current_weather = json_content.pop("main")

        json_content = data
        json_content = json_content.pop("main")
        temperature = json_content.pop("temp");
        temperature = int(temperature) - 273.5;
        temperature = int(temperature)
        pressure = json_content.pop("pressure")
        humidity = json_content.pop("humidity")
        # info = f"City: {City}, Current weather: {current_weather}, Temperature: {temperature}, pressure: {pressure}, humidity: {humidity}"
        data = {"City": City, "Current weather": current_weather, "Temperature": temperature, "Pressure": pressure,
                "Humidity": humidity}
    elif "message" in json_content:
        json_content = json_content.pop("message")
        if "city not found" == json_content:
            data = "Error"

    return data

def city_say(City="Kiev"):
    data = get_weather(City)
    if "Error" not in data:
        get_City = data.get("City")

        if get_City == "Kiev":
            get_City = "Киев"
        title = f"Погода для города {City}: \n"
    else:
        title = "Error"

    return title

def weather_say(City='Kiev'):
    data = get_weather(City)
    if "Error" not in data:
        get_CurrentWeather = data.get("Current weather")
        say_weather = ""

        if get_CurrentWeather == "Clouds":
            weather_dialogs = random.randint(0, 1)
            if weather_dialogs == 0:
                say_weather = "Ебаных облачек не наблюдаю"
            elif weather_dialogs == 1:
                say_weather = "Опачки, пропали облачки"
            else:
                "Empty"
        else:
            say_weather = "<Дописать код>"
    else:
        say_weather = "Error"
    return say_weather

def temperature_say(City="Kiev"):
    data = get_weather(City)
    if "Error" not in data:
        get_Temperature = data.get("Temperature")

        if 0 <= get_Temperature <= 10:
            say_temp = ", но сегодня довольно свежо. Не забудь шапочку)))0"
        elif 10 <= get_Temperature <= 20:
            say_temp = ". По температурке я бы сегодня захватил какую-нибудь толстовку."
        elif 20 <= get_Temperature <= 30:
            say_temp = ". Эх... Щас бы шашлычок у Скуза на даче."
        elif 30 <= get_Temperature <= 40:
            say_temp = ", но в такую жарень я бы не вышел из-под кондёра."
        elif get_Temperature >= 40:
            say_temp = ",но в печах Гитлера было прохладнее, короче выходи на свой еврейский риск."
        elif -10 <= get_Temperature <= 0:
            say_temp = ". Вода при такой температуре превратилась в лёд, а ты превратился в пидора."
        elif -20 <= get_Temperature <= -10:
            say_temp = ",но блять как же холодно сукааааааааааа"
        elif -30 <= get_Temperature <= -20:
            say_temp = ", а тебе норм в -200 на улице?????"
        elif -40 <= get_Temperature <= -30:
            say_temp = ". При такой температуре можно сделать кастрацию просто выйдя из-дому"
        else:
            say_temp = "Temperature is out of range."
    else:
        say_temp = "Error"
    return say_temp

def weather_payload(City="Kiev"):
    payload = city_say(City) + weather_say(City) + temperature_say(City)
    if "Error" in payload:
        payload = f"Error!!! No city named {City}."
    return payload

a = weather_payload("Lvivv")
print(a)