def register_routes(app):
    from .main_route import main_bp
    from .auth_route import auth_bp
    from .post_route import post_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(post_bp)