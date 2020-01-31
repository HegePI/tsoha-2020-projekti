from application import app, db, bcrypt
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import login_user, logout_user
from flask_bcrypt import Bcrypt
from application.user.UserModel import User
from application.login.LoginForm import LoginForm


@app.route("/login")
def login_form():
    return render_template("login/login.html", form=LoginForm())


@app.route("/login", methods=["POST"])
def login():

    form = LoginForm(request.form)
    username = form.username.data
    password = form.password.data

    user = User.query.filter_by(username=username).first()

    if user == None:

        error = "Kyseistä käyttäjää ei ole olemassa"

        return render_template("login/login.html", error=error, form=form)

    elif bcrypt.check_password_hash(user.password, password):

        login_user(user)
        return redirect(url_for("main_menu", user_id=user.id))

    else: 

        error = "Salasana väärin"
        return render_template("login/login.html", error=error, form=form)

@app.route("/logout")
def logout():
    
    logout_user()
    return redirect(url_for("index"))
