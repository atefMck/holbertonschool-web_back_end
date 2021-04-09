#!/usr/bin/env python3
""" Braaaaaahsqqdsqdsqdsq """


import bcrypt


def hash_password(password: str):
    """ Braaaaaahsqqdsqdsqdsq """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
