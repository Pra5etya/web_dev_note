from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from app.models.user_models import User
from app.models.post_models import Post

# import akses tabel dari Class yang telah dibuat
__all__ = ["db", "User", "Post"]
