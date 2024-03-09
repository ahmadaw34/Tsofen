from enum import Enum
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
    def __init__(self,email_addresses):
        """
        Constructor for Job class to initialize and define variables.
        """
        self._email_addresses=email_addresses
        self.__valid_emails=[]
        self.__invalid_emails = []
        self.__domains_json='Domains.json'
        self.__domains_dict = None
        self.__email_sender='awawdy.ahmad@gmail.com'
        self.__password = 'sbgg wwwp ovft chsc' #this password will be hidden in the future

    def _prerequisite(self):
        """
        check emails validation
        """
        try:
            email_address_format = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            email_addresses_list=str(self._email_addresses).split(',')

            self.__domains_dict=self._load_json_file(file_name=self.__domains_json)
            list_domains=self.__domains_dict["domains"]

            for addr in email_addresses_list:
                if re.match(email_address_format,addr) and addr[addr.find('@'):] in list_domains:
                    self.__valid_emails.append(addr)
                else:
                    self.__invalid_emails.append(addr)
                    logging.warning(f'Job._prerequisite: {addr} is invalid email format')

            if not self.__valid_emails:
                logging.error("no valid emails were found")
                raise ValueError('no valid emails were found')
        except Exception as e:
            raise Exception(f'Job._prerequisite: email validation failed with the following error: {e}')

    def _send_summarization_email(self,status):
        """
        send emails to valid addresses
        """
        try:
            if status is Status.Success:
                body = "The comparison has succeeded"
            else:
                body = "The comparison has failed"
            message = MIMEMultipart()
            message['From'] = self.__email_sender
            message['To'] = ', '.join(self.__valid_emails)
            message['Subject'] = 'Comparing Versions'
            message.attach(MIMEText(body, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.__email_sender, self.__password)
            server.send_message(message)
            server.quit()
            logging.info(f'email was sent successfully to {self.__valid_emails}')
        except Exception as e:
            raise Exception(f'there was an error in sending email with the following error: {e}')


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

