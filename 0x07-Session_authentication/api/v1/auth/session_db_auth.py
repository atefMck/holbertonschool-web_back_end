#!/usr/bin/env python3
""" Module of session based authentication with expiration
"""

import datetime
from models.user_session import UserSession
from api.v1.auth.session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """
        Session authentication Class with expiration
    """

    def create_session(self, user_id=None):
        """
            Create session with expiration in a file storage
        """
        if user_id is None:
            return None
        session_id = super().create_session(user_id)
        data = {
            'user_id': user_id,
            'session_id': session_id
        }
        user = UserSession(**data)
        user.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
            Returns a User ID based on a Session ID from file storage
        """
        if session_id is None:
            return None
        UserSession.load_from_file()
        user = UserSession.search(attributes={'session_id': session_id})
        if user is None or len(user) == 0:
            return None
        if (datetime.timedelta(seconds=self.session_duration)
            + user[0].created_at
                < datetime.datetime.now()):
            return None
        return user[0].user_id

    def destroy_session(self, request=None):
        """
            Destroys the UserSession based on the Session ID 
            from the request cookie
        """
        if request is None:
            return
        session_id = self.session_cookie(request)
        if session_id is None:
            return
        user = UserSession.search(attributes={'session_id': session_id})
        if user is None or len(user) == 0:
            return
        user[0].remove()
