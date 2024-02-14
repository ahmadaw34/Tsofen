import json
import os
from enums import Status


class CompareSourceTarget:

    def __init__(self):
        self.file_name = None

    def prerequisite(self):
        pass

    def run(self, file_name: str = "json_file.json"):
        self.file_name = file_name
        return self.__run_compare_process()

    def __run_compare_process(self):
        try:
            data = self.__load_json_file()
            source = None
            for d in data:
                if source is None:
                    source = d
                else:
                    for app in data[source]:
                        if app.find("version") != -1 and data[source][app] != data[d][app]:
                            return Status.Failure.value
        except Exception as e:
            print(f"Error: {e}")
            return Status.Failure.value
        return Status.Success.value

    def __load_json_file(self):
        file_path = os.getcwd()  # get current directory
        for root, dirs, files in os.walk(
                file_path):  # start walking toward from the current directory to find the file
            if self.file_name in files:
                file_path = os.path.join(root, self.file_name)
        with open(file_path, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)

    def send_email(self):
        pass
