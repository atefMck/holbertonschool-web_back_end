#!/usr/bin/env python3
"""Regex-ing"""
import csv
import logging
import mysql.connector
import os
import re
from typing import List
PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Constructor"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filter values from incoming log records"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns the log message obfuscated"""
    for field in fields:
        message = re.sub(r'{}=.*?{}'.format(field, separator),
                         '{}={}{}'.format(field, redaction, separator),
                         message)
    return message


def get_logger() -> logging.Logger:
    """Returns a logging.Logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    ch = logging.StreamHandler()
    ch.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(ch)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Returns a connector to the database"""
    dbUser = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    dbPassword = os.getenv('PERSONAL_DATA_DB_PASSWORD', ' ')
    dbHost = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    dbName = os.getenv('PERSONAL_DATA_DB_NAME')
    return mysql.connector.connection.MySQLConnection(user=dbUser,
                                                      password=dbPassword,
                                                      host=dbHost,
                                                      database=dbName)


def main() -> None:
    """Main"""
    # connect
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    num_fields = len(cursor.description)
    fields_names = [i[0] for i in cursor.description]
    logger = get_logger()
    for profile in cursor:
        message = ''
        for element in range(num_fields):
            msg += fields_names[element] + '=' + str(profile[element]) + ';'
        logger.info(msg)
    # close
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()  # !/usr/bin/env python3
"""Regex-ing"""
PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Constructor"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filter values from incoming log records"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns the log message obfuscated"""
    for field in fields:
        message = re.sub(r'{}=.*?{}'.format(field, separator),
                         '{}={}{}'.format(field, redaction, separator),
                         message)
    return message


def get_logger() -> logging.Logger:
    """Returns a logging.Logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    ch = logging.StreamHandler()
    ch.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(ch)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Returns a connector to the database"""
    dbUser = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    dbPassword = os.getenv('PERSONAL_DATA_DB_PASSWORD', ' ')
    dbHost = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    dbName = os.getenv('PERSONAL_DATA_DB_NAME')
    return mysql.connector.connection.MySQLConnection(user=dbUser,
                                                      password=dbPassword,
                                                      host=dbHost,
                                                      database=dbName)


def main() -> None:
    """MainMainMainMainMainMainMainMainMainMain"""
    # connect
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    num_fields = len(cursor.description)
    fields_names = [i[0] for i in cursor.description]
    logger = get_logger()
    for profile in cursor:
        message = ''
        for element in range(num_fields):
            msg += fields_names[element] + '=' + str(profile[element]) + ';'
        logger.info(msg)
    # close
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
