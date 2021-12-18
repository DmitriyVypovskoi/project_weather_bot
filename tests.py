import unittest
from main import start1
from main import weather1
from main import help1
from unittest import IsolatedAsyncioTestCase
from unittest.mock import MagicMock




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


class MyTestCase2(unittest.IsolatedAsyncioTestCase):
    async def test_something2(self):
        message = MagicMock()
        await start1(message=message)
        message.reply.assert_called_with("Привет, введите город в котором хотите узнать погоду")


class MyTestCase3(unittest.IsolatedAsyncioTestCase):
    async def test_something3(self):
        message = MagicMock()
        await weather1(message=message)
        message.reply.assert_called_with("Проверьте правильность введённых данных")



