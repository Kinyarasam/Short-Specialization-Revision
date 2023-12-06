#!/usr/bin/env python3
""" Definition of BasicAuth
"""
from api.v1.auth.auth import Auth
import base64
import re


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
        if decoded_base64_authorization_header is None:
            return (None, None)

        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)

        if re.search(':', decoded_base64_authorization_header) is None:
            return (None, None)

        return tuple(decoded_base64_authorization_header.strip().split(":"))
