#!/usr/bin/env python3
"""
filtered_logger File
"""

import os
import logging
import typing
import re
import mysql.connector


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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

def filter_datum(fields: typing.List[str], redaction: str, message: str, separator: str) -> str:
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
        pattern = re.search('{f}=(.*?){s}'.format(f=field,s=separator), message).group(0).split('=')[1][0:-1]
        message = re.sub(re.escape(pattern), redaction, message)
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

    formatter = RedactingFormatter(fields=PII_FIELDS)

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Creates a connector to the Database

    Returns:
        The connector to the database
    """
    db_host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_user = os.getenv('PERSONAL_DATA_DB_USERNAME', 'hbnb_revision')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME', "")
    db_pwd = os.getenv('PERSONAL_DATA_DB_PASSWORD', "")
    connection = mysql.connector.connect(
        host=db_host,
        port=3306,
        user=db_user,
        password=db_pwd,
        database=db_name,
    )
    return connection


def main():
    fields = "name,email,phone,ssn,password,ip,last_login,user_agent"
    columns = fields.split(",")
    query = "SELECT {} FROM users;".format(fields)
    info_logger = get_logger()
    connection = get_db()
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            record = map(
                lambda x: '{}={}'.format(x[0], x[1]),
                zip(columns, row))
            msg = '; '.join(list(record))
            log_record = logging.LogRecord(
                "user_data", logging.INFO, None, None, msg, None, None
            )
            info_logger.handle(log_record)


if __name__ == '__main__':
    main()
