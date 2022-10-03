from app import db
from datetime import datetime
import re


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30))
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    text = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        if self.title is None:
            self.title = self.text.split(".")[0]
        self.slug = self.genslug(self.title)
        if self.author is None:
            self.author = "Anonymous"


    def genslug(self, s):
        pattern = r'[^\w+]'
        return re.sub(pattern, '-', s)

    def __repr__(self):
        return "<Post: {}, title: {}>".format(self.id, self.title)
