#!/usr/bin/env python3
""" Module of session based authentication with expiration
"""

from models.user import User
from api.v1.auth.session_auth import SessionAuth
import os
import datetime


class SessionExpAuth(SessionAuth):
    """
        Session authentication Class with expiration
    """

    def __init__(self):
        """
            Class Constructor
        """
        super().__init__()
        self.session_duration = int(os.getenv('SESSION_DURATION', 0))

    def create_session(self, user_id=None):
        """
            Create session with expiration
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_dictionary = {
            'user_id': user_id,
            'created_at': datetime.datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
            Returns a User ID based on a Session ID
        """
        if session_id is None:
            return None
        if session_id not in self.user_id_by_session_id.keys():
            return None
        if self.session_duration <= 0:
            return self.user_id_by_session_id[session_id].get('user_id')
        if 'created_at' not in self.user_id_by_session_id[session_id].keys():
            return None
        if (datetime.timedelta(seconds=self.session_duration)
            + self.user_id_by_session_id[session_id].get('created_at')
                < datetime.datetime.now()):
            return None
        return self.user_id_by_session_id[session_id].get('user_id')
