#!/usr/bin/env python3
from api.v1.auth.auth import Auth
""" Definition of BasicAuth"""


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
