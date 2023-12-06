#!/usr/bin/env python3
""" Module to handle authentications
"""
from flask import request
from typing import List, TypeVar
import re


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        if path is None or not isinstance(excluded_paths, list) or len(excluded_paths) < 1:
            return True

        for p in excluded_paths:
            match = re.match(path, p)
            if not match:
                return True

        return False

    def authorization_header(self, request=None) -> str:
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        return request
