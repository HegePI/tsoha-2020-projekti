from application import app, db, bcrypt
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import current_user
from application.user.UserModel import User
from application.user.EditUserForm import EditUserForm

@app.route("/editUserInfo")
def edit_userinfo_form():
    return render_template("user/editUserInfo.html", form = EditUserForm())

@app.route("/editUserInfo", methods=["POST"])
def edit_userinfo():

    form = EditUserForm(request.form)

    new_username = form.username.data
    new_password = form.password.data

    hashed_new_password = bcrypt.generate_password_hash(new_password, 10)

    utf8_hashed_password = hashed_new_password.decode("utf-8", "ignore")

    user = User.query.get(current_user.id)

    user.username = new_username
    user.password = utf8_hashed_password
    
    db.session().commit()

    return redirect(url_for("main_menu"))
