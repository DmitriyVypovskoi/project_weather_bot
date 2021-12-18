from config import token
import requests
import datetime


def start(place):
    return weather(place, token)


def help():
    return(
          "***После начала работы бота введите название города,"
          " в котором вы хотите узнать состояние погоды на данный момент.\n"
          "Язык при этом не важен, можно указать как на русском так и на английском.\n"
          "Если найден не тот город попробуйте изменить первую букву на строчную "
          "если она была заглавной и наоборот***"
          )


def weather(place, token):
    try:
        # заимствованная часть проекта vvvv
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={place}&appid={token}&units=metric"
        )

        data = r.json()
        # заимствованная часть проекта ^^^^

        weather = data["weather"][0]["main"]

        if weather == "Clouds":
            weather = "Облачно" \
                      "\U00002601"

        elif weather == "Snow":
            weather = "Снег" \
                      "\U00002744"

        elif weather == "Mist":
            weather = "Туман" \
                      "\U0001F32B"

        elif weather == "Thunderstorm":
            weather = "Гроза" \
                      "\U0001F329"

        elif weather == "Drizzle":
            weather = "Мелкий дождь" \
                      "\U00002614"

        elif weather == "Clear":
            weather = "Облачно" \
                      "\U0001F31E"

        elif weather == "Rain":
            weather = "Дождь" \
                      "\U00002614"
        else:
            weather = weather

        place = data["name"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        vlag = data["main"]["humidity"]
        dav = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        len_day = sunset - sunrise
        country = data["sys"]["country"]

        return(f"Погода в городе: {place}\nCтрана: {country}\n{weather}\nТемпература: {int(temp)}С°\n"
               f"Ощущается как: {int(feels_like)}С°\n"
               f"Влажность: {vlag}%\n"
               f"Давление: {dav}мм.рт.ст\nСкорость ветра: {wind}м/с\nВосход солнца: {sunrise}\n"
               f"Закат солнца: {sunset}\nПродолжительность светового дня: {len_day}")

    except KeyError:
        return "Проверьте правильность введённых данных"


if __name__ == "__main__":
    start()
