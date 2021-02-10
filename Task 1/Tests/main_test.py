import sys
import json

sys.path.append("../prog")
from task_1_main import MakeStructure as ms


# Проверка корректности выполнения работы программы
def test_general():
    with open("../data_files/created/res_file.json", "r", encoding="utf-8") as file:
        test_result = json.load(file)
    with open("StructureWithValues.json", "r", encoding="utf-8") as file:
        correct_result = json.load(file)

    if test_result == correct_result:
        print("PASSED: General test")
    else:
        print("FAILED: General test")


# Проверка подгрузки данных их файлов
def test_get_data_from_file(case, files):
    for res, file in files:
        if res != case.get_data_from_file(file):
            print("FAILED: Loading data test\nОшибка обработки файла", file)
            break
        else:
            pass
    print("PASSED: Loading data test")


def test_get_value_from_file(case, test_data, test_json):
    tmp = case.values
    case.values = test_json
    for test_id, test_res in test_data:
        res = case.get_value_from_file(test_id)
        if res != test_res:
            print("FAILED: Get value from file test")
            case.values = tmp
            break
        else:
            pass
    case.values = tmp
    print("PASSED: Get value from file test ")


# Создаем инстанс класса MakeStructure
test_test = ms()

# Проверка обработки кривых входных данных
test_files = [({"pos1": "info", "pos2": "Info"}, "correct.json"), ("Input error", "incorrect_1.json")]
test_get_data_from_file(test_test, test_files)

# Проверка функции, вынимающий значения из файла Values.json
test_list = [{"id": 12, "value": 6}, {"id": 1158, "value": "Some text"}, {"id": 78, "value": "6"}]
test_get_value_from_file(test_test, [(12, 6), (78, "6"), (100, "")], test_list)

# Проверка корректного выполнения работы программы: соответствия созданного файла ожидаемому
test_general()
