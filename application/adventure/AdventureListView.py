from application import app, db
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from application.adventure.AdventureModel import Adventure

@app.route("/<int:id>/adventures")
@login_required
def list_users_adventures(id):
    return render_template("/adventure/showUsersAdventures.html", 
    ongoing_adventures=Adventure.query.filter_by(dungeon_master=current_user.id, ongoing=1).all(),
    finished_adventures=Adventure.query.filter_by(dungeon_master=current_user.id, ongoing=0).all())