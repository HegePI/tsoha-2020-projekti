from application import app, db, bcrypt, login_required
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_bcrypt import Bcrypt
from flask_login import current_user
from application.character.NewCharacterForm import NewCharacterForm
from application.character.CharacterModel import Character
from application.adventure.AdventureModel import Adventure

@app.route("/newCharacter/<int:adventure_id>/")
@login_required(role="ANY")
def join_adventure_form(adventure_id):

    adventure = Adventure.query.filter_by(id=adventure_id).first()

    if adventure.dungeon_master == current_user.id:
        return render_template("menu.html", all_adventures=Adventure.list_adventures(), error="Olet seikkailun Dungeon Master")

    adventure = Adventure.query.filter_by(id=adventure_id).first()
    return render_template("/character/newCharacter.html", form = NewCharacterForm(), adventure=adventure)

@app.route("/newCharacter/<int:adventure_id>/", methods=["POST"])
@login_required(role="ANY")
def create_new_character(adventure_id):
    
    adventure = Adventure.query.filter_by(id=adventure_id).first()
    form = NewCharacterForm(request.form)

    c_name = form.character_name.data
    c_class = form.character_class.data
    c_race = form.character_race.data
    c_strength = form.character_strength.data
    c_dexterity = form.character_dexterity.data
    c_inteligence = form.character_inteligence.data
    c_faith = form.character_faith.data
    c_health = form.character_health.data
    c_mana = form.character_mana.data

    character = Character(c_name, c_class, c_race, c_strength, c_dexterity, 
    c_inteligence, c_faith, c_health, c_mana, current_user.id, adventure_id)

    db.session().add(character)
    db.session().commit()

    message = "Hahmo luotiin onnistuneesti"
    return render_template("/character/newCharacter.html", form = NewCharacterForm(), adventure=adventure, message = message)

