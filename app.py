"""
module app.py contains main portfolio code
dont forget to set up ENV variables FLASK_APP, FLASK_ENV before run
"""

from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")
db = SQLAlchemy(app)

"""
data base entities section
"""

# test entity
# TODO delete later
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


# TODO create actual db entities
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)


class Technology(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)


"""
проект (название, общее описание, ссылка на гитхаб, описание фич, скриншоты, технологии, доп информация);
технология (название, общее описание);
"""

"""
routes section
"""


@app.route('/')
def index():
    Users = User.query.all()
    return render_template("add_user.html", Users=Users)


@app.route('/about/<string:name>')
def about(name):
    return 'about' + name


@app.route('/post_user', methods=['POST'])
def post_user():
    user = User(request.form['username'], request.form['email'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))


class HelloWorld(Resource):
    def get(self, name):
        return {'hello': name}


api.add_resource(HelloWorld, '/api/<string:name>')

if __name__ == '__main__':
    app.run()
