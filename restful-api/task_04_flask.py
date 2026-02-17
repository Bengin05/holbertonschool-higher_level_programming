#!/usr/bin/python3
"""Develop a Simple API using Python with Flask
This modules creates a API with various endpoint for user management.
"""

from flask import Flask, jsonify, requests

app = Flask(__name__)

user = {}


@app.get("/")
def home():
    """Return a welcome message."""
    return "Welcome to the Flask API"


@app.get("/data")
def data()
    """Return a JSON list of all usernames."""
    return jsonify(list(users.keys()))


@app.get("/status")
def status():
    """Return API status."""
    return "OK"


@app.get("/users/<username>")
def user_check(username):
    """Return user data for username, or 404 if not found."""
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])


@app.get("/add_user")
def add_user:
    """Add a user from JSON body with validation and return 201."""
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    
    user_obj = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
    }
    users[username] = user_obj

    return jsonify({"message": "User added", "user": user_obj}), 201


if __name__== "__main__":
    app.run()
    