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
                parameter["value"] = self.get_value_from_values(parameter["id"], parameter['values'])
                # print(parameter)
            else:
                parameter["value"] = self.get_value_from_file(parameter["id"])

        self.make_result_file()

    def get_value_from_values(self, par_id, values):
        value = self.get_value_from_file(par_id)
        value = values[0]['title'] if value == "" else value
        # print(value)
        if "params" in values[0]:
            print(values[0])
            self.set_param_value(values)
        return value

    def set_param_value(self, params):
        for parameter in params:
            if "values" in parameter.keys():
                parameter["value"] = self.get_value_from_values(parameter["id"], parameter['values'])
            else:
                pass
                parameter["value"] = self.get_value_from_file(parameter["id"])

    def get_value_from_file(self, elem_id):
        for elem in self.values:
            if elem["id"] == elem_id:
                return elem["value"]
        return ""


test_case = MakeStructure()
test_case.make_structure()
