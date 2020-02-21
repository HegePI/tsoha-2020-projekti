from application import app, db, login_required
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import current_user
from application.adventure.AdventureModel import Adventure

@app.route("/<int:id>/adventures")
@login_required
def list_users_adventures(id):
    return render_template("/adventure/showUsersAdventures.html", 
    ongoing_adventures=Adventure.query.filter_by(dungeon_master=current_user.id, ongoing=1).all(),
    finished_adventures=Adventure.query.filter_by(dungeon_master=current_user.id, ongoing=0).all())

@app.route("/deleteAdventure/<int:adventure_id>", methods=["POST"])
@login_required(role="ANY")
def delete_adventure(adventure_id):
    
    adventure = Adventure.query.filter_by(id=adventure_id).first()

    db.session.delete(adventure)

    try:
        db.session.commit()
        message = "Seikkailu poistettiin onnistuneesti"
        return render_template("/adventure/showUsersAdventures.html", 
        ongoing_adventures=Adventure.query.filter_by(dungeon_master=current_user.id, ongoing=1).all(),
        finished_adventures=Adventure.query.filter_by(dungeon_master=current_user.id, ongoing=0).all(),
        message=message)
    except exc.SQLAlchemyError:
        message = "Jotain meni pieleen"
        return render_template("/adventure/showUsersAdventures.html", 
        ongoing_adventures=Adventure.query.filter_by(dungeon_master=current_user.id, ongoing=1).all(),
        finished_adventures=Adventure.query.filter_by(dungeon_master=current_user.id, ongoing=0).all(),
        message=message)