#!/usr/bin/env python3
""" Braaaaaahsqqdsqdsqdsq """


from typing import List
import re
import logging
import os
import mysql.connector


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Braaaaaahsqqdsqdsqdsq """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Braaaaaahsqqdsqdsqdsq """
        message = logging.Formatter(self.FORMAT).format(record)
        return filter_datum(self.fields, self.REDACTION, message,
                            self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Braaaaaahsqqdsqdsqdsq """
    return (separator.join(text if text.split("=")[0] not in fields
                           else re.sub("=(.*)$", "=" + redaction, text)
                           for text in message.split(separator)))


def get_logger() -> logging.Logger:
    """ Braaaaaahsqqdsqdsqdsq """

    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler = logging.StreamHandler().setLevel(
        logging.INFO).setFormatter(formatter)

    logger = logging.getLogger("user_data").setLevel(logging.INFO)
    logger.propagate = False
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Braaaaaahsqqdsqdsqdsq """

    db_username = os.getenv('PERSONAL_DATA_DB_USERNAME', "root")
    db_password = os.getenv('PERSONAL_DATA_DB_PASSWORD', "")
    db_host = os.getenv('PERSONAL_DATA_DB_HOST', "localhost")
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')
    return mysql.connector.connect(user=db_username,
                                   password=db_password,
                                   host=db_host,
                                   database=db_name)
