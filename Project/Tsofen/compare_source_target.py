import json
import os
from enums import Status
import re
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class CompareSourceTarget:

    def __init__(self):
        self.file_name = None
        self.__data=None

    def run(self, file_name: str = "json_file.json"):
        """
        this function is the entering point of the job.
        """
        self.file_name = file_name
        self.__prerequisite()
        return self.__run_compare_process()

    def __prerequisite(self):
        try:
            version_format = r'^\d{2,}\.\d{2}\.\d{2,}$'
            self.__data = self.__load_json_file()
            for d in self.__data:
                for app in self.__data[d]:
                    if app.find('version') != -1 and not re.match(version_format, self.__data[d][app]):
                        raise ValueError(self.__data[d][app] + ' doesnt match the expected version format')
            logging.debug(f"prerequisite: Success")
        except Exception as e:
            logging.error(f"prerequisite: {e}")
            raise Exception(e)

    def __run_compare_process(self):
        try:
            source = None
            for d in self.__data:
                if source is None:
                    source = d
                else:
                    for app in self.__data[source]:
                        if app.find("version") != -1 and self.__data[source][app] != self.__data[d][app]:
                            logging.error(f"__run_compare_process: {source}:{app}:{self.__data[source][app]} != {d}:{app}:{self.__data[d][app]}")
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
