from application import app, db
from flask import Flask, flash, redirect, render_template, request, url_for
from application.user.models import User


@app.route("/login")
def login_form():
    return render_template("login/login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter_by(username=username, password=password).first()

    if user == None:
        error = "Käyttäjänimi tai salasana väärin."
        return render_template("login/login.html", error=error)
    else:
        message = "kirjauduttiin onnistuneesti!"
        return render_template("menu/menu.html", message=message)
