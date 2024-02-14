import json
import os
import enums

class compare_source_target:
    def prerequisite(self):
        return
    def Run(self,fileName):
        return self.run_compare_process(fileName)
    def run_compare_process(self,fileName):
        try:
            filePath = os.getcwd()  # get current directory
            for root, dirs, files in os.walk(filePath):  # start walking toward from the current directory to find the file
                if fileName in files:
                    filePath = os.path.join(root, fileName)
            with open(filePath, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
            source = None
            for d in data:
                if source is None:
                    source = d
                else:
                    for app in data[source]:
                        if app.find("version") != -1 and data[source][app] != data[d][app]:
                            return enums.Status.Failure.value
        except Exception as e:
            print(f"Error: {e}")
            return enums.Status.Failure.value
        return enums.Status.Success.value
    def send_email(self):
        return