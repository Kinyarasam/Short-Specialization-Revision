#!/usr/bin/env python3
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes the input password using bcrypt with a random salt.

    Args:
        password (str): The password to be hashed.

    Returns:
        bytes: The salted and hashed passwords as a byte string.
    """
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password

def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validates the provided password matches the hashed password

    Args:
        hashed_password (bytes): The hashed password to be checked.
        password (str): The password to be validated.

    Returns:
        bool: True if the password is valid, False otherwise
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
