from application import app, db, bcrypt, login_required
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_bcrypt import Bcrypt
from flask_login import current_user
from application.character.NewCharacterForm import NewCharacterForm
from application.character.CharacterModel import Character
from application.adventure.AdventureModel import Adventure

@app.route("/editCharacter/<int:character_id>/")
@login_required(role="ANY")
def edit_character_form(character_id):
    character = Character.query.filter_by(id=character_id).first()
    character_form = NewCharacterForm()

    return render_template("/character/editCharacter.html", form = NewCharacterForm(), 
    character=Character.query.filter_by(id=character_id).first())

@app.route("/editCharacter/<int:character_id>/", methods=["POST"])
@login_required(role="ANY")
def edit_character(character_id):

    form = NewCharacterForm(request.form)

    character = Character.query.filter_by(id=character_id).first()

    character.character_name=form.character_name.data
    character.character_class=form.character_class.data
    character.character_race=form.character_race.data
    character.character_strength=form.character_strength.data
    character.character_dexterity=form.character_dexterity.data
    character.character_inteligence=form.character_inteligence.data
    character.character_faith=form.character_faith.data
    character.character_health=form.character_health.data
    character.character_mana=form.character_mana.data

    db.session().add(character)
    db.session().commit()

    message = "Hahmon muokkaus onnistui!"

    return render_template("/character/editCharacter.html", form = NewCharacterForm(), 
    character=Character.query.filter_by(id=character_id).first(), message=message)