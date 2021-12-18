import unittest
from bot import weather
from bot import help
from bot import start
from config import token


class Test1(unittest.TestCase):

    def test3(self):
        self.assertNotEqual((weather("краснодар", token)), "Проверьте правильность введённых данных")

    def test4(self):
        self.assertNotEqual((weather("краснодар", token)), "Проверьте правильность введённых данных")

    def test5(self):
        self.assertIn(weather("масква", token), "Проверьте правильность введённых данных")

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
