from application import app, db, bcrypt, login_required
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import current_user, logout_user
from application.item.ItemModel import Item
from application.item.ItemForm import ItemForm

@app.route("/item/editItem/<int:id>")
@login_required(role="ANY")
def edit_item_form(id):
    item = Item.query.filter_by(id=id).first()
    return render_template("item/editItem.html", item=item, form=ItemForm())

@app.route("/item/editItem/<int:id>/", methods=["POST"])
@login_required(role="ANY")
def edit_item(id):

    form = ItemForm(request.form)

    new_item_name = form.item_name.data
    new_item_description = form.item_description.data

    existing_item = Item.query.filter_by(item_name=new_item_name).first()

    if existing_item.id == id:
        item = Item.query.get(id)

        item.item_name = new_item_name
        item.item_description = new_item_description
    
        db.session().commit()

        return render_template("item/editItem.html", item=existing_item, form=ItemForm(), message="Esineen tiedot muutettiin onnistuneesti!")
    
    else:
        return render_template("item/editItem.html", item=existing_item, form=ItemForm(), message="Esine on jo olemassa kyseisellä nimellä...")
