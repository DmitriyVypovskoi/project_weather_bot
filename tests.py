import unittest
import tg_bot
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
