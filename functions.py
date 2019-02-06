import requests
import random
import constants

#Возвращает сырые данные в json от Weather API
def get_raw_weather_data(City="Kiev"):
    url = f'http://api.openweathermap.org/data/2.5/weather?appid={constants.WEATHER_API_KEY}&q={City}'
    data = requests.get(url).json()

    return data

#Возвращает обработанные данные в json от Weather API
def get_weather(City="Kiev"):
    url = f'http://api.openweathermap.org/data/2.5/weather?appid={constants.WEATHER_API_KEY}&q={City}'
    data = requests.get(url).json()
    json_content = data

    if "message" not in json_content:
        json_content = json_content.pop("weather")
        json_content = json_content.pop()
        icon = json_content.pop("icon")
        current_weather = json_content.pop("main")

        json_content = data
        json_content = json_content.pop("main")
        temperature = json_content.pop("temp");
        temperature = int(temperature) - 273.5;
        temperature = int(temperature)
        pressure = json_content.pop("pressure")
        humidity = json_content.pop("humidity")

        data = {"City": City, "Current weather": current_weather, "Temperature": temperature, "Pressure": pressure,
                "Humidity": humidity}
    elif "message" in json_content:
        json_content = json_content.pop("message")
        if "city not found" == json_content:
            data = "Error"

    return data

#Возвращает title для сообщения
def city_say(City="Kiev"):
    data = get_weather(City)
    if "Error" not in data:
        get_City = data.get("City")

        if get_City == "Kiev":
            get_City = "Киев"
        title = f"Погода для города {get_City}: \n\n"
    else:
        title = "Error"

    return title

def weather_say(City='Kiev'):
    data = get_weather(City)
    if "Error" not in data:
        get_CurrentWeather = data.get("Current weather")

        if get_CurrentWeather == "Clear":
            weather_dialogs = random.randint(0, 1)
            if weather_dialogs == 0:
                say_weather = "Ебаных облачек не наблюдаю.\n"
            elif weather_dialogs == 1:
                say_weather = "Опачки, пропали облачки.\n"
            else:
                say_weather = "Empty"
        elif get_CurrentWeather == "Snow":
            weather_dialogs = random.randint(0, 3)
            if weather_dialogs == 0:
                say_weather = "Долго не было зимы…\nЖдали, волновались.\nА за сутки выпал снег…\nКак же заебались.\n"
            elif weather_dialogs == 1:
                say_weather = "Посидел вчера в сугробе,\nПоморозил себе нос,\nИнтерес к моей особе\nВмиг у милого возрос.\n"
            elif weather_dialogs == 2:
                say_weather = "Вот и выпал вдруг снежок,\nИ упал на носик.\nА ты сидишь все за компом,\nБездарь-недоносик.\n"
            elif weather_dialogs == 3:
                say_weather = "***Let it snow, let it snow, let it snow***"
            else:
                say_weather = "Empty"
        elif get_CurrentWeather == "Thunderstorm":
            weather_dialogs = random.randint(0, 1)
            if weather_dialogs == 0:
                say_weather = "Thunderstorm"
            elif weather_dialogs == 1:
                say_weather = "Thunderstorm"
            else:
                say_weather = "Empty"
        elif get_CurrentWeather == "Drizzle":
            weather_dialogs = random.randint(0, 1)
            if weather_dialogs == 0:
                say_weather = "Drizzle"
            elif weather_dialogs == 1:
                say_weather = "Drizzle"
            else:
                say_weather = "Empty"

        elif get_CurrentWeather == "Rain":
            weather_dialogs = random.randint(0, 1)
            if weather_dialogs == 0:
                say_weather = "Rain"
            elif weather_dialogs == 1:
                say_weather = "Rain"
            else:
                say_weather = "Empty"
        elif get_CurrentWeather == "Fog":
            weather_dialogs = random.randint(0, 1)
            if weather_dialogs == 0:
                say_weather = "Mist1"
            elif weather_dialogs == 1:
                say_weather = "Fog1"
            else:
                say_weather = "Empty"
        elif get_CurrentWeather == "Mist":
            weather_dialogs = random.randint(0, 1)
            if weather_dialogs == 0:
                say_weather = "Fog2"
            elif weather_dialogs == 1:
                say_weather = "Mist2"
            else:
                say_weather = "Empty"
        elif get_CurrentWeather == "Clouds":
            weather_dialogs = random.randint(0, 1)
            if weather_dialogs == 0:
                say_weather = str(emoji_print("Cloud"))*3 + "\nClouds "
            elif weather_dialogs == 1:
                say_weather = "Clouds "
            else:
                say_weather = "Empty"
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

def emoji_print(emoji):
    emoji = constants.weather_emoji.get(emoji)

    return emoji


Gorod = "Lviv"
b = get_weather(Gorod)
print(b)
a = weather_say(Gorod)
print(a)