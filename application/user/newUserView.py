from application import app, db
from flask import Flask, flash, redirect, render_template, request, url_for
from application.user.models import User


@app.route("/newUser")
def newUser_form():
    return render_template("user/new.html")


@app.route("/newUser", methods=["POST"])
def newUser_create():
    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter_by(username=username).first()

    if user != None:
        error = "Käyttäjänimi on jo käytössä."
        return render_template("user/new.html", error=error)
    else:
        user = User(username, password)
        db.session().add(user)
        db.session().commit()
        message = "käyttäjä luotiin onnistuneesti!"
        return render_template("login/login.html", message=message)
