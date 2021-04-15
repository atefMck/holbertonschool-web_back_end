#!/usr/bin/env python3
"""
App module
"""


from flask import Flask, jsonify
from flask.globals import request
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def greetings():
    """ Greetings """
    return jsonify({'message': 'Bienvenue'})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """ Register """
    email = request.form['email']
    password = request.form['password']
    try:
        user = AUTH.register_user(email, password)
        return jsonify({
            "email": email,
            "message": "user created"})
    except ValueError:
        return jsonify({
            "message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000")
