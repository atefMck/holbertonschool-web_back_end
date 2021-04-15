#!/usr/bin/env python3
"""
App module
"""


from flask import Flask, jsonify, abort, redirect
from flask.globals import request
from flask.helpers import make_response
from flask.wrappers import Response
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


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """ Login method """
    email = request.form['email']
    password = request.form['password']
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = make_response(jsonify({{"email": email,
                                           "message": "logged in"}}))
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """
    User logout function.
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    else:
        AUTH.destroy_session(user.id)
        return redirect('/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
