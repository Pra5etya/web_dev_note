from app.models import db

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    body = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)

    def __repr__(self):
        return f"<Post {self.title}>"
