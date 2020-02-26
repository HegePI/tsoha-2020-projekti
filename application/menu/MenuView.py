from application import app, db, login_required
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import current_user
from application.user.UserModel import User
from application.adventure.AdventureModel import Adventure


@app.route("/menu")
@login_required(role="ANY")
def main_menu():
    return render_template("menu.html", all_adventures=Adventure.list_adventures())
