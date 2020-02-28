from application import app, db, login_required
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import current_user
from application.character.CharacterModel import Character
from application.character.characterItemModel import characterItem
from application.item.ItemModel import Item

@app.route("/character/<int:character_id>/addItem/")
@login_required(role="ANY")
def add_item_form(character_id):
    return render_template("character/addItem.html", character=Character.query.filter_by(id=character_id).first(), items=Item.query.all())

@app.route("/character/<int:character_id>/addItem/<int:item_id>/", methods=["POST"])
@login_required(role="ANY")
def add_item(character_id, item_id):
    character = Character.query.filter_by(id=character_id).first()
    item = Item.query.filter_by(id=item_id).first()
    CI = characterItem()

    CI.character = character
    CI.item = item

    character.items.append(CI)
    item.characters.append(CI)

    db.session.add(character)
    db.session.add(item)

    db.session.commit()

    message="Esine lisätty"
    return render_template("character/showUsersCharacters.html", characters=Character.find_users_characters(current_user.id), message=message)