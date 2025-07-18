from flask import request

def log_middleware(response):
    print(f"{request.method} {request.path} -> {response.status}")
    return response
