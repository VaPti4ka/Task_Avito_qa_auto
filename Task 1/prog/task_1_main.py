import json


class MakeStructure:
    filepath_origin = "../data_files/original/"
    filepath_created = "../data_files/created/"


    def __init__(self):
        self.setting = self.get_data_from_file(self.filepath_origin + "setting.json")
        self.error_messg = {"error": self.setting["error"]}
        self.testcase = self.get_data_from_file(self.filepath_origin + self.setting["testcase_2"])
        self.values = self.get_data_from_file(self.filepath_origin + self.setting["value"])["values"]
        self.result = None

        if "Input error" in self.__dict__.values():
            self.make_error_file()
            print("Поданы некорректные файлы, завершение работы программы.")
            raise SystemExit


    # Возвращает содержимое JSON файл
    def get_data_from_file(self, filename):
        try:
            with open(filename, "r", encoding='utf-8') as file:
                return json.load(file)
        except:
            self.error_messg["error"]["broken_file"] = filename
            return ("Input error")



    # Записываем исправленную структуру в файл. Если не было - создается
    def make_result_file(self):
        with open(self.filepath_created + self.setting["result"], "w", encoding="utf-8") as file:
            json.dump(self.result, file, indent=2, ensure_ascii=False)

    # Рекурсивная фун-я исправления структуры
    def make_structure(self):
        self.result = self.testcase.copy()
        self.set_param_value(self.result["params"])
        self.make_result_file()

    # Проверяет текущий уровень на наличие вложенных values, записывает значение в value
    def set_param_value(self, params):
        for parameter in params:
            if "values" in parameter.keys():
                parameter["value"] = self.get_value_from_values(parameter["id"], parameter['values'])
            elif "value" in parameter.keys():
                parameter["value"] = self.get_value_from_file(parameter["id"])


    # Проверяет текущий уровень на наличие вложенных params, выбирает и возвращает значение values
    def get_value_from_values(self, par_id, values):
        val_id = self.get_value_from_file(par_id)
        value = ""
        for val in values:
            if val['id'] == val_id:
                value = val['title']
            if "params" in val:
                self.set_param_value(val["params"])
        if value == "" and val_id != "":
            value = values[0]['title']
        return value

    # Получает значение values из Values.json
    def get_value_from_file(self, elem_id):
        for elem in self.values:
            if elem["id"] == elem_id:
                return elem["value"]
        return ""

    # Обрабатывает некорректно введенные данные
    def make_error_file(self):
        with open(self.filepath_created + self.setting["error_messg"], "w", encoding="utf-8") as file:
            json.dump(self.error_messg, file, indent=2, ensure_ascii=False)



test_case = MakeStructure()
test_case.make_structure()
