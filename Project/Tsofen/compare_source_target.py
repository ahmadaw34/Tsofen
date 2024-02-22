import json
import os
from enums import Status
import re
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class CompareSourceTarget:

    def __init__(self):
        self.file_name = None

    def prerequisite(self):
        try:
            version_format = r'^\d{2,}\.\d{2}\.\d{2,}$'
            data = self.__load_json_file()
            for d in data:
                for app in data[d]:
                    if app.find('version') != -1 and not re.match(version_format, data[d][app]):
                        raise ValueError(data[d][app] + ' doesnt match the expected version format')
            logging.debug(f"prerequisite: Success")
            return Status.Success.value
        except Exception as e:
            logging.error(f"prerequisite: {e}")

    def run(self, file_name: str = "json_file.json"):
        self.file_name = file_name
        if self.prerequisite() == Status.Success.value and self.__run_compare_process() == Status.Success.value:
            logging.debug(f"run: Success")
            return Status.Success.value
        else:
            logging.error(f"run: Failure")
            return Status.Failure.value

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
                            logging.error(f"__run_compare_process: {source}:{app}:{data[source][app]} != {d}:{app}:{data[d][app]}")
                            return Status.Failure.value
        except Exception as e:
            logging.error(f"__run_compare_process: {e}")
            return Status.Failure.value
        logging.debug(f"__run_compare_process: Success")
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
