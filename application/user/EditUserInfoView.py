from application import app, db, bcrypt
from flask import Flask, flash, redirect, render_template, request, url_for
from application.user.UserModel import User

@app.route("/editUserInfo/<user_id>/")
def edit_userinfo_form(user_id):
    return render_template("user/editUserInfo.html", user = User.query.get(user_id))

@app.route("/editUserInfo/<user_id>/", methods=["POST"])
def edit_userinfo(user_id):
    new_username = request.form.get("username")
    new_password = request.form.get("password")

    hashed_new_password = bcrypt.generate_password_hash(new_password, 10)
    utf8_hashed_password = hashed_new_password.decode("utf-8", "ignore")
    user = User.query.get(user_id)
    user.username = new_username
    user.password = utf8_hashed_password
    db.session().commit()

    message = "Käyttäjän tiedot päivitetty"

    return redirect(url_for("main_menu", user_id=user_id))
