
from Job import *


class CompareSourceTarget(Job):

    def __init__(self,email_addresses, version_file_name: str = "json_file.json"):
        """
        constructor
        """
        super().__init__(email_addresses=email_addresses)
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
                    if app.find('version') != -1 and not re.match(version_format, self._data[d][app]):
                        self.send_email(Status.Failure.value, True)
                        raise ValueError(self._data[d][app] + ' doesnt match the expected version format')
            logging.debug(f"CompareSourceTarget.prerequisite: Success")
        except Exception as e:
            logging.error(f"CompareSourceTarget.prerequisite: {e}")
            raise Exception(e)

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
                            self.send_email(Status.Failure.value, True)
                            return Status.Failure.value
        except Exception as e:
            logging.error(f"__run_compare_process: {e}")
            self.send_email(Status.Failure.value, True)
            return Status.Failure.value
        logging.debug(f"__run_compare_process: Success")
        self.send_email(Status.Success.value,True)
        return Status.Success.value

    def send_email(self,status:enums.Status=Status.Failure.value,send_email:bool=False):
        self._send_summarization_email(status,send_email)
