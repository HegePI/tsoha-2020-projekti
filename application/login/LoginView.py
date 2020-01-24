from application import app, db, bcrypt
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_bcrypt import Bcrypt
from application.user.Models import User


@app.route("/login")
def login_form():
    return render_template("login/login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter_by(username=username).first()

    if user == None:
        error = "Kyseistä käyttäjää ei ole olemassa"
        return render_template("login/login.html", error=error)
    elif bcrypt.check_password_hash(user.password, password):
        return redirect(url_for("main_menu", user_id=user.id))
    else: 
        error = "Salasana väärin"
        return render_template("login/login.html", error=error)
