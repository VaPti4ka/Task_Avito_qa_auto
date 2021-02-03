import json


class MakeStructure:
    filepath_origin = "../data_files/original/"
    filepath_created = "../data_files/created/"

    def __init__(self):
        self.setting = self.get_file_data(self.filepath_origin + "setting.json")
        self.testcase = self.get_file_data(self.filepath_origin + self.setting["testcase_2"])
        self.values = self.get_file_data(self.filepath_origin + self.setting["value"])
        self.result = None

    @staticmethod
    def get_file_data(filename):
        with open(filename) as file:
            return json.load(file)

    def make_result_file(self):
        with open(self.filepath_created + "res_file.json", "w", encoding="utf-8") as file:
            json.dump(self.result, file, indent=2)


test_case = MakeStructure()
