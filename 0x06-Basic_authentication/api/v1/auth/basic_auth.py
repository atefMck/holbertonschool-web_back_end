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

    def decode_base64_authorization_header(
         self,
         base64_authorization_header: str) -> str:
        """
            returns the decoded value of a Base64 string
        """
        if (base64_authorization_header is None
                or type(base64_authorization_header) is not str):
            return None
        try:
            return (base64.b64decode(base64_authorization_header)
                    .decode('utf-8'))
        except Exception:
            return None

    def extract_user_credentials(
         self,
         decoded_base64_authorization_header: str) -> (str, str):
        """
            returns the user credentials
        """
        if (decoded_base64_authorization_header is None
                or type(decoded_base64_authorization_header) is not str
                or ":" not in decoded_base64_authorization_header):
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(":"))
