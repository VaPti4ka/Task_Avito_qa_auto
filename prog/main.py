import json


class MakeStructure:
    filepath_origin = "../data_files/original/"
    filepath_created = "../data_files/created/"

    def __init__(self):
        self.setting = self.get_file_data(self.filepath_origin + "setting.json")
        self.testcase = self.get_file_data(self.filepath_origin + self.setting["testcase_2"])
        self.values = self.get_file_data(self.filepath_origin + self.setting["value"])["values"]
        self.result = None

    @staticmethod
    def get_file_data(filename):
        with open(filename, encoding='utf-8') as file:
            return json.load(file)

    def make_result_file(self):
        with open(self.filepath_created + "res_file.json", "w", encoding="utf-8") as file:
            json.dump(self.result, file, indent=2)

    def make_structure(self):
        self.result = self.testcase.copy()
        for parameter in self.result["params"]:
            if "values" in parameter.keys():
                pass
            else:
                parameter["value"] = self.get_value_from_values(parameter["id"])
                print("Параметр ->", parameter)

    def get_value_from_values(self, elem_id):
        for elem in self.values:
            if elem["id"] == elem_id:
                return elem["value"]
        return ""


test_case = MakeStructure()
test_case.make_structure()
