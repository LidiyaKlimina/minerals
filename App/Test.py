import os
print(os.getcwd())
from minerals.utils.one import get_vitamins_input
from minerals.testing.asserts import assertTrue


def test01():
    v = get_vitamins_input()
    assertTrue(False, "Не работает ввод витаминов")


test01()