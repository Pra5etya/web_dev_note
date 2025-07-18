from flask import request, jsonify, g

def auth_middleware():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Unauthorized"}), 401
    if token != "Bearer SECRET123":
        return jsonify({"error": "Invalid token"}), 403
    g.user = "user_from_token"
