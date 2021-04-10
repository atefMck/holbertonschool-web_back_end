#!/usr/bin/env python3
""" Module of authentication
"""


from typing import List, TypeVar
from flask import request


class Auth:
    """
        Authentication Class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            Checks if authentication is required
        """
        if path is None:
            return True
        return not any(path in ex_path for ex_path in excluded_paths)

    def authorization_header(self, request=None) -> str:
        """
            Undetirmined
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
            Undetirmined
        """
        return None