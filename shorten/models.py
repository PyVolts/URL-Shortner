from shorten import db


class urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(200), nullable=False)
    short_url = db.Column(db.String(100), nullable=False, unique=True)
