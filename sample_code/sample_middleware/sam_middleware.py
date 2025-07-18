from flask import request, abort

# WSGI Middleware
class MyMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print("==> WSGI Middleware: Request intercepted")
        return self.app(environ, start_response)

# Before Request: Logging
def log_request():
    print(f"==> Logging: {request.method} {request.url}")

# Before Request: API Key check
def api_key_check(expected_key):
    key = request.headers.get("X-API-KEY")
    if key != expected_key:
        abort(401, description="Invalid API Key")

# After Request: Add custom header
def add_custom_header(response):
    response.headers["X-App-Version"] = "1.0.0"
    return response
