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
        print("General test PASSED")
    else:
        print("General test FAILED")


# Проверка подгрузки данных их файлов
def test_get_data_from_file(case, files):
    # 0 - Удалось, 1 - Ошибка

    for res, file in files:
        if res != case.get_data_from_file(file):
            print("Loading data test FAILED\nОшибка обработки файла", file)
            break
        else:
            pass
    print("Loading data test PASSED")


# Создаем инстанс класса MakeStructure
test_test = ms()

# Проверка обработки кривых входных данных
test_files = [({"pos1": "info", "pos2": "Info"}, "correct.json"), ("Input error", "incorrect_1.json")]
test_get_data_from_file(test_test, test_files)


