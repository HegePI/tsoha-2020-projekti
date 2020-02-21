from application import app, db, bcrypt, login_required
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_bcrypt import Bcrypt
from flask_login import current_user
from application.character.NewCharacterForm import NewCharacterForm
from application.character.CharacterModel import Character
from application.adventure.AdventureModel import Adventure
from sqlalchemy import exc 

@app.route("/usersCharacters/")
@login_required(role="ANY")
def list_users_characters():
    return render_template("/character/showUsersCharacters.html",
     characters=Character.find_users_characters(user_id=current_user.id))

@app.route("/allCharacters")
@login_required(role="ADMIN")
def list_all_characters():
    return render_template("/character/showAllCharacters.html", characters=Character.find_all_characters())

@app.route("/deleteCharacter/<int:character_id>/", methods=["POST"])
@login_required(role="ANY")
def delete_character(character_id):
    
    character = Character.query.filter_by(id=character_id).first()

    db.session.delete(character)

    try:
        db.session.commit()
        message = "Hahmo poistettiin onnistuneesti"
        return render_template("/character/showUsersCharacters.html",
        characters=Character.query.filter_by(account_id=current_user.id).all(), message=message)
    except exc.SQLAlchemyError:
        message = "Jotain meni pieleen"
        return render_template("/character/showUsersCharacters.html",
        characters=Character.query.filter_by(account_id=current_user.id).all(), message=message)
