from application import app, db, bcrypt
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_bcrypt import Bcrypt
from flask_login import current_user, login_required
from application.character.NewCharacterForm import NewCharacterForm
from application.character.CharacterModel import Character
from application.adventure.AdventureModel import Adventure

@app.route("/usersCharacters/")
@login_required
def list_characters():
    return render_template("/character/showAllCharacters.html",
     characters=Character.find_users_characters(current_user.id))