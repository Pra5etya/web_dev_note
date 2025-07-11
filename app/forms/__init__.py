# Import semua form yang ada
from .register_flask import RegisterForm
from .login_flask import LoginForm
from .post_flask import PostForm

# Tentukan apa yang boleh diimport dari package forms
__all__ = ["RegisterForm", "LoginForm", "PostForm"]
