import json
import os
import re
import enums
from enums import Status

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Job:
    def __init__(self):
        """
        constructor
        """
        self._email_addresses=None
        self.__valid_emails=[]
        self.__invalid_emails = []
        self._email_file_name=None
        self._data = None
        self.__email_sender='awawdy.ahmad@gmail.com'
        self.__password = 'sbgg wwwp ovft chsc'
    def _prerequisite(self):
        """
        check emails validation
        """
        try:
            email_address_format = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            self._data=self._load_json_file(self._email_file_name)
            list_domains=self._data["domains"]
            email_addresses_list=str(self._email_addresses).split(',')
            for addr in email_addresses_list:
                if re.match(email_address_format,addr):
                    if addr[addr.find('@'):] in list_domains:
                        self.__valid_emails.append(addr)
                    else:
                        self.__invalid_emails.append(addr)
                else:
                    logging.warning(f'Job._prerequisite: {addr} is invalid email format')
        except Exception as e:
            raise Exception(e)

    def _send_summarization_email(self,status,send_email):
        """
        send emails to valid addresses
        """
        try:
            if send_email:
                if status is Status.Success.value:
                    body = "The comparison has succeeded"
                else:
                    body = "The comparison has failed"
                if len(self.__valid_emails) == 0 and len(self.__invalid_emails) == 0:
                    logging.error("there is no emails to send to")
                    raise ValueError("there is no emails to send to")
                message = MIMEMultipart()
                message['From'] = self.__email_sender
                emails=self.__valid_emails+self.__invalid_emails
                message['To'] = ', '.join(emails)
                message['Subject'] = 'ComparingVersions'
                message.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(self.__email_sender, self.__password)
                server.send_message(message)
                server.quit()
                for invalid in self.__invalid_emails:
                    logging.warning(f'email sent to invalid email ({invalid})')
                logging.debug(f'email send successfully')
        except Exception as e:
            raise Exception(e)


    def _load_json_file(self,file_name):
        """
        loads json file
        """
        file_path = os.getcwd()  # get current directory
        for root, dirs, files in os.walk(
                file_path):  # start walking toward from the current directory to find the file
            if file_name in files:
                file_path = os.path.join(root, file_name)
        if not os.path.exists(file_path):
            logging.error(f"file does not exist")
        if os.path.getsize(file_path) == 0:
            logging.error(f"file is empty")
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json_file.read()
            if not data.strip():
                logging.error(f"file contains only whitespace")
                raise ValueError(file_name+' contains only whitespace')
        with open(file_path, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)

