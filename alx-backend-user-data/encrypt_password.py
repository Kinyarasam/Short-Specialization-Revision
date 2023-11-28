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
