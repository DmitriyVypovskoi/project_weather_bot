import unittest
from main import start1
from main import weather1
from main import help1
from unittest import IsolatedAsyncioTestCase
from unittest.mock import MagicMock
import json
from mock import Mock, patch, MagicMock

async def async_magic():
    pass

MagicMock.__await__ = lambda x: async_magic().__await__()


class MyTestCase(unittest.IsolatedAsyncioTestCase):
    async def test_something(self):
        message = MagicMock()
        await help1(message=message)
        message.answer.assert_called_with("После начала работы бота введите название города, в котором вы хотите узнать состояние погоды на данный момент.\n"
                                          "Язык при этом не важен, можно указать как на русском так и на английском.\n"
                                          "Если найден не тот город попробуйте изменить первую букву на строчную "
                                          "если она была заглавной и наоборот")


    async def test_something2(self):
        message = MagicMock()
        await start1(message=message)
        message.reply.assert_called_with("Привет, введите город в котором хотите узнать погоду")


    async def test_something3(self):
        message = MagicMock()
        await weather1(message=message)
        message.reply.assert_called_with("Проверьте правильность введённых данных")

    @patch('requests.get')
    async def test_weather(self, get):
        txt = '{"coord":{"lon":38.9769,"lat":45.0328},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"base":"stations","main":{"temp":2.2,"feels_like":2.2,"temp_min":1.68,"temp_max":2.7,"pressure":1015,"humidity":92},"visibility":10000,"wind":{"speed":1,"deg":280},"clouds":{"all":75},"dt":1639843462,"sys":{"type":2,"id":2012251,"country":"RU","sunrise":1639803462,"sunset":1639835023},"timezone":10800,"id":542420,"name":"Krasnodar","cod":200}'
        response = MagicMock()
        response.json.return_value = json.loads(txt)
        get.return_value = response
        message = MagicMock()
        await weather1(message=message)
        message.reply.assert_called_with("Погода в городе: Krasnodar\nCтрана: RU\nОблачно☁\nТемпература: 2С°\nОщущается как: 2С°\nВлажность: 92%\nДавление: 1015мм.рт.ст\nСкорость ветра: 1м/с\nВосход солнца: 2021-12-18 07:57:42\nЗакат солнца: 2021-12-18 16:43:43\nПродолжительность светового дня: 8:46:01")



