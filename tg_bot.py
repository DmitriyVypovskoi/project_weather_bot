import requests
import datetime
from config import tg_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import token



bot = Bot(token=tg_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start1(message: types.Message):
    await message.reply("Привет, введите город в котором хотите узнать погоду")


@dp.message_handler(commands=["help"])
async def help1(message: types.Message):
    await message.answer("После начала работы бота введите название города,"
                         " в котором вы хотите узнать состояние погоды на данный момент.\n"
                         "Язык при этом не важен, можно указать как на русском так и на английском.\n"
                         "Если найден не тот город попробуйте изменить первую букву на строчную "
                         "если она была заглавной и наоборот")

@dp.message_handler()
async def weather1(message: types.Message):

    try:
        # заимствованная часть проекта vvvv
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={token}&units=metric"
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

        await message.reply(f"Погода в городе: {place}\n{weather}\nТемпература: {int(temp)}С°\nОщущается как: {int(feels_like)}С°\n"
                            f"Влажность: {vlag}%\n"
                            f"Давление: {dav}мм.рт.ст\nСкорость ветра: {wind}м/с\nВосход солнца: {sunrise}\n"
                            f"Закат солнца: {sunset}\nПродолжительность светового дня: {len_day}")

    except KeyError:
        await message.reply("Проверьте правильность введённых данных")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)