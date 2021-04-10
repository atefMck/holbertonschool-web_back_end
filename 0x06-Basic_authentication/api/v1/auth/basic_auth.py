#!/usr/bin/env python3
""" Module of basic authentication
"""


from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """
        Basic authentication Class
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
            returns the Base64 part of the Authorization
            header for a Basic Authentication
        """
        if (authorization_header is None
                or type(authorization_header) is not str
                or authorization_header.split(" ")[0] != 'Basic'):
            return None
        return authorization_header.split(" ")[1]
