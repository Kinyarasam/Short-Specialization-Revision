#!/usr/bin/env python3
from api.v1.views import app_views
from flask import jsonify, request
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session():
    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or email == '':
        return jsonify({"error": "email missing"}), 400

    if password is None or password == '':
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": email})
    if not users or users == []:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if user.is_valid_password(password):
            from api.v1.app import auth

            session_id = auth.create_session(user.id)
            user_dict = jsonify(user.to_json())

            session_name = os.getenv('SESSION_NAME')
            user_dict.set_cookie(session_name, session_id)

            return user_dict
    return jsonify({"error": "wrong password"}), 401
