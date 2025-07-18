from .auth import auth_middleware
from .logging import log_middleware
from .security import security_headers_middleware

def register_middleware(app): 
    @app.before_request
    def before_request():
        result = auth_middleware()
        if result:
            return result

    @app.after_request
    def after_request(response):
        response = log_middleware(response)
        response = security_headers_middleware(response)
        return response