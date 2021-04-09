#!/usr/bin/env python3
""" Braaaaaahsqqdsqdsqdsq """


from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str):
    """ Braaaaaahsqqdsqdsqdsq """
    r = []
    for text in message.split(separator):
        r.append(text if text.split("=")[0] not in fields else re.sub(
            "=(.*)$", "=" + redaction, text))
    return ";".join(r)
