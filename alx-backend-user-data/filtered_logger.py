#!/usr/bin/env python3
"""
filtered_logger File
"""

import logging
import typing
import re



class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: typing.List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        msg = super(RedactingFormatter, self).format(record)
        txt = filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)
        return txt

def filter_datum(fields: typing.List, redaction: str, message: str, separator: str) -> str:
    """
    Function to Obfuscate a message

    Args:
        fields (List): list of strings representing all fields to obfuscate.
        redaction (String): A string to represent to what the field will be obfuscated
        message (String): the log line.
        separator (String): String representing what character is separating all fields in the log file.

    Returns:
        (String): obfuscated message.
    """
    for field in fields:
        pattern = re.search(r'{f}=(.*?){s}'.format(f=field,s=separator), message).group(0).split('=')[1][0:-1]
        message = re.sub(pattern, redaction, message)
    return message

def get_logger() -> logging.Logger:
    """
    Function to create and configure a logger.

    Returns
        - logging.Logger: Configured logger object.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    formatter = 
