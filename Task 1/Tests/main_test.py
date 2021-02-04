import sys
import json

sys.path.append("../prog")
from task_1_main import MakeStructure as ms


def test_general():
    with open("../data_files/created/res_file.json", "r", encoding="utf-8") as file:
        test_result = json.load(file)
    with open("StructureWithValues.json", "r", encoding="utf-8") as file:
        correct_result = json.load(file)

    if test_result == correct_result:
        print("General test PASSED!")
    else:
        print("General test FAILED")


def test_get_data_from_file():
    pass


# Создаем инстанс класса MakeStructure
test_test = ms()

test_general()
