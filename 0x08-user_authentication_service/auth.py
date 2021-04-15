#!/usr/bin/env python3
"""
Auth module
"""


from app import AUTH
from sqlalchemy.orm.exc import NoResultFound

from db import DB
import bcrypt
import uuid

from user import User


def _hash_password(password: str) -> bytes:
    """
    Hashes str password
    """
    return bcrypt.hashpw(
        password.encode('utf-8'),
        bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generates uuid
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Constructor
        """
        self._db = DB()

    def register_user(
            self,
            email: str, password: str) -> User:
        """Registers a user in database
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(
                "User {} already exists".format(email))
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """Validates credentials
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                if bcrypt.checkpw(
                        password.encode('utf-8'),
                        user.hashed_password):
                    return True
                return False
        except Exception:
            return False

    def create_session(self, email: str) -> str:
        """Creates session
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                session_id = _generate_uuid()
                self._db.update_user(user.id, session_id=session_id)
                return session_id
        except Exception:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """Get user from session id
        """
        try:
            user = self._db.find_user_by(session_id=session_id)
            if user:
                return user
            return None
        except Exception:
            return None

    def destroy_session(self, user_id: int):
        """Destroys user session
        """
        try:
            self._db.update_user(user_id, session_id=None)
            return None
        except Exception:
            return None
