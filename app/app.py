from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
# from db_inter import db

# postdb = db("postdb")



app = Flask(__name__)
app.config.from_object(Configuration)


db = SQLAlchemy(app)



import view

from posts.blueprint import posts
app.register_blueprint(posts, url_prefix='/blog')
from debug.blueprint import debug
app.register_blueprint(debug, url_prefix='/debug')


if __name__ == 'main':
	app.run(debug=True)
