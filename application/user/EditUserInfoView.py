from application import app, db, bcrypt, login_required
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import current_user, logout_user
from application.user.UserModel import User
from application.user.EditUserForm import EditUserForm

@app.route("/editUserInfo")
@login_required(role="ANY")
def edit_userinfo_form():
    return render_template("user/editUserInfo.html", form = EditUserForm())

@app.route("/editUserInfo", methods=["POST"])
@login_required(role="ANY")
def edit_userinfo():

    form = EditUserForm(request.form)

    new_username = form.username.data
    new_password = form.password.data

    existing_user = User.query.filter_by(username=new_username).first()

    if not existing_user:
        hashed_new_password = bcrypt.generate_password_hash(new_password, 10)

        utf8_hashed_password = hashed_new_password.decode("utf-8", "ignore")

        user = User.query.get(current_user.id)

        user.username = new_username
        user.password = utf8_hashed_password
    
        db.session().commit()

        return render_template("user/editUserInfo.html", form = EditUserForm(), message="Käyttäjän tiedot muutettiin onnistuneesti!")
    
    else:
        return render_template("user/editUserInfo.html", form = EditUserForm(), message="Kyseinen käyttäjänimi on jo käytössä!")

@app.route("/editUserInfo/delete", methods=["POST"])
@login_required(role="ANY")
def delete_user_account():

    deleted_user = User.query.filter_by(id=current_user.id).first()

    db.session.delete(deleted_user)
    db.session.commit()
    
    logout_user()
    return redirect(url_for("index"))
