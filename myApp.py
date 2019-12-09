from flask import Flask, render_template, request
import os
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
App = Flask(__name__)
# print(__file__)
# print(project_dir)

database_file = "sqlite:///{}".format(os.path.join(project_dir, "record.db"))

App.config["SQLALCHEMY_DATABASE_URI"] = database_file
App.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(App)


class User(db.Model):
    name = db.Column(db.String(40), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(40), unique=False, nullable=False)
    city = db.Column(db.String(40), unique=False, nullable=False)
    position = db.Column(db.String(40), unique=False, nullable=False)


# db.create_all()


@App.route('/')
def index():
    return render_template('index.html', methods=["POST", "GET"])


@App.route('/signup')
def signup():
    return render_template('adminoption.html')


@App.route('/signup1')
def signup1():
    return render_template('admin_signup.html')


@App.route('/test', methods=["POST", "GET"])
def test():
    if request.method == "POST":
        user1 = User()
        user1.name = request.form['username']
        user1.password = request.form['pass']
        user1.city = request.form['city']
        user1.position = request.form['post']
        db.session.add(user1)
        db.session.commit()

        return render_template('admin_signup.html')


@App.route('/users')
def users():
    myUsers = User.query.all()
    return render_template('users.html', users=myUsers)


@App.route('/studentusers')
def studentusers():
    myUsers = User.query.all()
    return render_template('studentusers.html', users=myUsers)


@App.route('/teacherusers')
def teacherusers():
    myUsers = User.query.all()
    return render_template('teacherusers.html', users=myUsers)


@App.route('/deleteUser', methods=["POST"])
def delete_user():
    user_name = request.form['target_user']
    user_found = User.query.filter_by(name=user_name).first()
    db.session.delete(user_found)
    db.session.commit()
    myUsers = User.query.all()
    return render_template('users.html', users=myUsers)


@App.route('/updateUser', methods=["POST"])
def update_user():
    user_name = request.form['target_user']
    user_city = request.form['target_city']
    user_found = User.query.filter_by(name=user_name).first()
    user_found.city = user_city
    db.session.add(user_found)
    db.session.commit()
    myUsers = User.query.all()
    return render_template('users.html', users=myUsers)


@App.route('/updateUser1', methods=["POST"])
def update_user1():
    user_name = request.form['target_user']
    user_passw = request.form['target_password']
    user_found = User.query.filter_by(name=user_name).first()
    user_found.password = user_passw
    db.session.add(user_found)
    db.session.commit()
    myUsers = User.query.all()
    return render_template('studentusers.html', users=myUsers)


@App.route('/updateUser2', methods=["POST"])
def update_user2():
    user_name = request.form['target_user']
    user_pas = request.form['target_password']
    user_found = User.query.filter_by(name=user_name).first()
    user_found.password = user_pas
    db.session.add(user_found)
    db.session.commit()
    myUsers = User.query.all()
    return render_template('studentusers.html', users=myUsers)


@App.route('/student')
def student():
    return render_template('student_signup.html')


@App.route('/test1', methods=["POST", "GET"])
def test1():
    if request.method == "POST":
        user1 = User()
        user1.name = request.form['username']
        user1.password = request.form['pass']
        user1.city = request.form['city']
        user1.position = request.form['post']
        db.session.add(user1)
        db.session.commit()

        return render_template('student_signup.html')


@App.route('/teacher')
def teacher():
    return render_template('teacher_signup.html')


@App.route('/test2', methods=["POST", "GET"])
def test2():
    if request.method == "POST":
        user1 = User()
        user1.name = request.form['username']
        user1.password = request.form['pass']
        user1.city = request.form['city']
        user1.position = request.form['post']
        db.session.add(user1)
        db.session.commit()

    return render_template('teacher_signup.html')


@App.route('/login', methods=["POST", "GET"])
def login():
    return render_template('login.html')


@App.route('/test3', methods=["POST", "GET"])
def test3():
    if request.method == "POST":
        password = request.form['pass']
        user_name = request.form['username']

    user = User.query.filter_by(name=user_name).first()
    if user:
        if user.password == password and user.position == 'student':
            return render_template('studentdashboard.html')
        elif user.password == password and user.position == 'teacher':
            return render_template('teacherdashboard.html')
        elif user.password == password and user.position == 'admin':
            return render_template('admindashboard.html')
        else:
            return '<h1>Credentials Incorrect</h1>'


App.run()
