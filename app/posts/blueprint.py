from flask import Blueprint, render_template, request

from models.db_inter import Post
from app import db

posts = Blueprint('posts', __name__,  template_folder='templates')


@posts.route('/')
def index():
	postss = Post.query.all()
	return render_template('posts/index.html', n="blogger", posts=postss)

@posts.route('/newpost')
def newpost():
	return render_template('posts/newpost.html', n="poster")

@posts.route('/newpost/send', methods=["POST"])
def send():
	if len(request.form["text"]) == 0:
		return "Type something in text at least", 200
	np = Post(text=request.form["text"], title=request.form["title"])
	db.session.add(np)
	db.session.commit()
	return "ok", 200

@posts.route('/<slug>')
def viewpost(slug):
	post = Post.query.filter(Post.slug==slug).first()
	return render_template('posts/postview.html', post=post, n="reader")
