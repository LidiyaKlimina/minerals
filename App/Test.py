import os
print(os.getcwd())
from minerals.utils.one import get_vitamins_input
from minerals.testing.asserts import assertTrue

def test_vitmins_input():
    # given
    inputs = [
        "a, b1,b12",
        ",a,b1,b2,b3,b5,b6,b9,b12,c,d,e,k,fe,mg,cu,ca,p,zn",
        ]

    outputs = [
        ["a", "b1", "b12"],
        ["", "a","b1","b2","b3","b5","b6","b9","b12","c","d","e","k","fe","mg","cu","ca","p","zn"]
    ]

    # when
    i = 0
    for input in inputs:

        result = get_vitamins_input(input)
        print(result)
        # then
        assertTrue(result == outputs[i], "Не работает ввод витаминов")
        i += 1

test_vitmins_input()