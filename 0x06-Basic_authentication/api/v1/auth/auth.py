#!/usr/bin/env python3
""" Module of authentication
"""


from typing import List, TypeVar
from flask import request
import re


class Auth:
    """
        Authentication Class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            Checks if authentication is required
        """
        if path is None or excluded_paths is None:
            return True
        return not any(re.search(path, ex_path) for ex_path in excluded_paths)

    def authorization_header(self, request=None) -> str:
        """
            Return Authorization header if it exists
        """
        return (None
                if request is None or 'Authorization' not in request.headers
                else request.headers['Authorization']
                )

    def current_user(self, request=None) -> TypeVar('User'):
        """
            Undetirmined
        """
        return None
