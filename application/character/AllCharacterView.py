from application import app, db, bcrypt, login_required
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_bcrypt import Bcrypt
from flask_login import current_user
from application.character.NewCharacterForm import NewCharacterForm
from application.character.CharacterModel import Character
from application.adventure.AdventureModel import Adventure

@app.route("/usersCharacters/")
@login_required(role="ANY")
def list_users_characters():
    return render_template("/character/showUsersCharacters.html",
     characters=Character.find_users_characters(current_user.id))

@app.route("/allCharacters")
@login_required(role="ADMIN")
def list_all_characters():
    return render_template("/character/showAllCharacters.html", characters=Character.find_all_characters())