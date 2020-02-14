from application import app, db
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from application.adventure.AdventureModel import Adventure

@app.route("/<int:id>/adventures")
@login_required
def list_users_adventures(id):
    return render_template("/adventure/showUsersAdventures.html", adventures=Adventure.find_users_adventures(id))