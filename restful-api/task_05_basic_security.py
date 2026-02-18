#!/usr/bin/python3
"""
API Security and Authentication Techniques:
- Basic Auth protected route: /basic-protected
- JWT login route: /login
- JWT protected route: /jwt-protected
- Admin-only route (JWT + role check): /admin-only

All JWT authentication errors return 401 for checker consistency.
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt,
    get_jwt_identity,
    jwt_required,
)
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "super-secret-key-change-me"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


@auth.verify_password
def verify_password(username, password):
    """Verify Basic Auth credentials against hashed passwords."""
    user = users.get(username)
    if not user:
        return False
    return check_password_hash(user["password"], password)


@app.get("/basic-protected")
@auth.login_required
def basic_protected():
    """Basic Auth protected endpoint."""
    return "Basic Auth: Access Granted"


@app.post("/login")
def login():
    """Login with username/password and receive a JWT access token."""
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "Bad username or password"}), 401

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Bad username or password"}), 401

    token = create_access_token(
        identity=username,
        additional_claims={"role": user["role"]},
    )
    return jsonify({"access_token": token})


@app.get("/jwt-protected")
@jwt_required()
def jwt_protected():
    """JWT protected endpoint."""
    return "JWT Auth: Access Granted"


@app.get("/admin-only")
@jwt_required()
def admin_only():
    """Admin-only endpoint protected by JWT + role check."""
    username = get_jwt_identity()
    claims = get_jwt()
    role = claims.get("role")

    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403

    if not username or username not in users:
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
