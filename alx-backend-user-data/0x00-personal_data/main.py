#!/usr/bin/env python3
"""
Main file
"""
filter_datum = __import__('filtered_logger').filter_datum

fields = ["password", "date_of_birth"]
messages = [
    "name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;",
    "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"
]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))

print('='*20)
print()

import logging
import re

RedactingFormatter = __import__('filtered_logger').RedactingFormatter

message = "name=Bob;email=bob@dylan.com;ssn=000-123-000;password=bobby2019;"
log_record = logging.LogRecord("my_logger", logging.INFO, None, None, message, None, None)
formatter = RedactingFormatter(fields=("email", "ssn", "password"))
print(formatter.format(log_record))
print('='*20)
print()

get_logger = __import__('filtered_logger').get_logger
PII_FIELDS = __import__('filtered_logger').PII_FIELDS

print(get_logger.__annotations__.get('return'))
print("PII_FIELDS: {}".format(len(PII_FIELDS)))

print('='*20)
print()

get_db = __import__('filtered_logger').get_db

db = get_db()
cursor = db.cursor()
cursor.execute("SELECT COUNT(*) FROM users;")
for row in cursor:
    print(row[0])
cursor.close()
db.close()

print('='*20)
print()


hash_password = __import__('encrypt_password').hash_password

password = "MyAmazingPassw0rd"

is_valid = __import__('encrypt_password').is_valid
encrypted_password = hash_password(password)
print(encrypted_password)
print(is_valid(encrypted_password, password))