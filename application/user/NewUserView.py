from application import app, db, bcrypt
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_bcrypt import Bcrypt
from application.user.UserModel import User
from application.user.form import UserForm
from application.login.LoginForm import LoginForm


@app.route("/newUser")
def new_user_form():
    return render_template("user/new.html", form = UserForm())


@app.route("/newUser", methods=["POST"])
def create_new_user():

    form = UserForm(request.form)

    if not form.validate():
        return render_template("user/new.html", form=form)

    username = form.username.data
    password = form.password.data

    user = User.query.filter_by(username=username).first()

    if user != None:

        error = "Käyttäjänimi on jo käytössä."
        return render_template("user/new.html", error=error, form=UserForm())

    else:

        hashed_password = bcrypt.generate_password_hash(password, 10)
        utf8_hashed_password = hashed_password.decode("utf-8", "ignore")

        user = User(username, utf8_hashed_password)

        db.session().add(user)
        db.session().commit()

        message = "käyttäjä luotiin onnistuneesti!"
        
        return render_template("login/login.html", message=message, form=LoginForm())
