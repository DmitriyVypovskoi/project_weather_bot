import unittest
import tg_bot
#from bot import help
#from bot import start
#from bot import weather
from unittest import mock
from config import token
from unittest.mock import MagicMock

class Test2(unittest.TestCase):
    @mock.patch('tg_bot.bot')
    def test_main_encode(self, tg_bot):
        chat = MagicMock(id=123)
        message = MagicMock(text="/help", chat=chat)
        tg_bot.mess(message)
        tg_bot.send_message.assert_called_with(123,
                                                f"***После начала работы бота введите название города, в котором вы хотите узнать состояние погоды на данный момент.\nЯзык при этом не важен, можно указать как на русском так и на английском.\nЕсли найден не тот город попробуйте изменить первую букву на строчную если она была заглавной и наоборот***")

"""
class Test1(unittest.TestCase):

    def test3(self):
        self.assertNotEqual((weather("краснодар", token)), "Проверьте правильность введённых данных")

    def test4(self):
        self.assertNotEqual((weather("краснодар", token)), "Проверьте правильность введённых данных")

    def test5(self):
        self.assertIn(weather("ошибка", token), "Проверьте правильность введённых данных")

    def test6(self):
        self.assertNotEqual(weather("MOSCOW", token), "Проверьте правильность введённых данных")

    def test7(self):
        self.assertIn(weather("НЬЮЙОРК", token), "Проверьте правильность введённых данных")


class Test2(unittest.TestCase):

    def test_other2(self):
        self.assertEqual(help(), "***После начала работы бота введите название города,"
                         " в котором вы хотите узнать состояние погоды на данный момент.\n"
                         "Язык при этом не важен, можно указать как на русском так и на английском.\n"
                         "Если найден не тот город попробуйте изменить первую букву на строчную "
                         "если она была заглавной и наоборот***")

    def test_other3(self):
        self.assertNotEqual(start("Voronezh"), "Проверьте правильность введённых данных")
"""