from application import app, db, bcrypt, login_required
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import current_user
from application.item.ItemForm import ItemForm
from application.item.ItemModel import Item

@app.route("/newItemForm/")
@login_required(role="ANY")
def new_item_form():
    return render_template("/item/newItem.html", form = ItemForm())

@app.route("/createItem/", methods=["POST"])
@login_required(role="ANY")
def create_new_item():
    
    form = ItemForm(request.form)

    name = form.item_name.data
    description = form.item_description.data

    print(description)
    
    item = Item(name, description)

    db.session().add(item)
    db.session().commit()

    message = "Esine luotiin onnistuneesti"
    return render_template("/item/newItem.html", form = ItemForm(), message=message)
