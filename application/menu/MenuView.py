from application import app, db
from flask import Flask, flash, redirect, render_template, request, url_for
from application.user.UserModel import User


@app.route("/menu/<user_id>")
def main_menu(user_id):
    return render_template("menu/menu.html", user = User.query.get(user_id))
