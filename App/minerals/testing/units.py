import unittest
from App.minerals.utils.one import get_vitamins_input


class MainTests(unittest.TestCase):

    def test_vitamins_input(self):
        # given

        # when
        r = get_vitamins_input()

        # then
        self.assertTrue(r != None, msg="Не работает ввод витаминов")
