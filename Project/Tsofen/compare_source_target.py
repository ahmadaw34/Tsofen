
from Job import *


class CompareSourceTarget(Job):

    def __init__(self,email_addresses, version_file_name: str = "json_file.json",send_email:bool=False):
        """
        constructor
        """
        super().__init__(email_addresses=email_addresses)
        self.send_email=send_email
        self.__version_file_name = version_file_name

    def run(self):
        """
        this function is the entering point of the job.
        """
        self._prerequisite()
        return self.__run_compare_process()

    def _prerequisite(self):
        """
        check versions format *.nn.*
        """
        super()._prerequisite()

        try:
            version_format = r'^\d{2,}\.\d{2}\.\d{2,}$'
            self._data = self._load_json_file(self.__version_file_name)
            for d in self._data:
                for app in self._data[d]:
                    if app.find('version') != -1 and not re.match(version_format, self._data[d][app]) and self.send_email:
                        self.send_email_to_user(status=Status.Failure)
                        raise ValueError(self._data[d][app] + ' doesnt match the expected version format')
            logging.info("CompareSourceTarget.prerequisite: Success")
        except Exception as e:
            logging.error(f"CompareSourceTarget.prerequisite: _prerequisite failed with the following error: {e}")
            raise Exception(f"CompareSourceTarget.prerequisite: _prerequisite failed with the following error: {e}")

    def __run_compare_process(self):
        """
        compare between app's versions
        """
        try:
            source = None
            for d in self._data:
                if source is None:
                    source = d
                else:
                    for app in self._data[source]:
                        if app.find("version") != -1 and self._data[source][app] != self._data[d][app]:
                            logging.error(f"__run_compare_process: {source}:{app}:{self._data[source][app]} != {d}:{app}:{self._data[d][app]}")
                            self.send_email_to_user(Status.Failure)
                            return Status.Failure.value
        except Exception as e:
            logging.error(f"__run_compare_process: comparing failed with the following error: {e}")
            return Status.Failure.value
        
        logging.info("__run_compare_process: Success")
        self.send_email_to_user(Status.Success)
        return Status.Success.value

    def send_email_to_user(self,status):
        self._send_summarization_email(status=status)
