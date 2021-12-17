from config import token
import requests
import datetime
from pprint import pprint



def weather(place, token):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={place}&appid={token}&units=metric"
        )

        data = r.json()

        pprint(data)

        place = data["name"]
        feels_like = data["main"]["feels_like"]
        temp = data["main"]["temp"]
        vlag = data["main"]["humidity"]
        dav = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        len_day = sunset - sunrise

        print(f"Погода в городе: {place}\nТемпература: {int(temp)}С°\nОщущается как: {int(feels_like)}С°\nВлажность: {vlag}%\n"
              f"Давление: {dav}мм.рт.ст\nСкорость ветра: {wind}м/с\nВосход солнца: {sunrise}\n"
              f"Закат солнца: {sunset}\nПродолжительность светового дня: {len_day}")

    except KeyError:
        print("Проверьте правильность введённых данных")


def start():
    place = input("Введите наименование населённого пункта: ")
    weather(place, token)


if __name__ == "__main__":
    start()