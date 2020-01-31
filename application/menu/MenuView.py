from application import app, db
from flask import Flask, flash, redirect, render_template, request, url_for
from application.user.UserModel import User


@app.route("/menu")
def main_menu():
    return render_template("menu/menu.html")
