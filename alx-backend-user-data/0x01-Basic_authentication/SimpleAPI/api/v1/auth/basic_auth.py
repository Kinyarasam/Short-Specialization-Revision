#!/usr/bin/env python3
""" Definition of BasicAuth
"""
import base64
import re
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """ Implement Basic Authorization protocal methods"""

    def __init__(self) -> None:
        super().__init__()

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        auth_data = authorization_header.strip().split()
        if auth_data[0] != 'Basic':
            return None

        return auth_data[-1]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            return base64.b64decode(base64_authorization_header).decode('utf-8')
        except:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        delimeter = ':'
        if decoded_base64_authorization_header is None:
            return (None, None)

        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)

        if re.search(':', decoded_base64_authorization_header) is None:
            return (None, None)

        record = decoded_base64_authorization_header.strip().split(delimeter)
        email = record[0]
        passwd = delimeter.join(record[1:])

        return tuple(email, passwd)

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({"email": user_email})
            if not users or users == []:
                return None
            for u in users:
                if u.is_valid_password(user_pwd):
                    return u
            return None
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        token = self.extract_base64_authorization_header(auth_header)

        if token is None:
            return None

        decoded_token = self.decode_base64_authorization_header(token)

        if decoded_token is None:
            return None

        email, passwd = self.extract_user_credentials(decoded_token)
        return self.user_object_from_credentials(email, passwd)
