#!/usr/bin/env python3
""" Braaaaaahsqqdsqdsqdsq """


from typing import List
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List):
        """ Braaaaaahsqqdsqdsqdsq """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Braaaaaahsqqdsqdsqdsq """
        message = logging.Formatter(self.FORMAT).format(record)
        return filter_datum(self.fields, self.REDACTION, message, self.SEPARATOR)

def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Braaaaaahsqqdsqdsqdsq """
    r = []
    for text in message.split(separator):
        r.append(text if text.split("=")[0] not in fields else re.sub(
            "=(.*)$", "=" + redaction, text))
    return ";".join(r)
