from application import app, db, bcrypt, login_required
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import current_user
from application.item.NewItemForm import NewItemForm
from application.item.ItemModel import Item

@app.route("/newItemForm/")
@login_required(role="ANY")
def new_item_form():
    return render_template("/item/newItem.html", form = NewItemForm())

@app.route("/createItem/", methods=["POST"])
@login_required(role="ANY")
def create_new_item():
    
    form = NewItemForm(request.form)

    name = form.item_name.data
    description = form.item_description.data

    print(description)
    
    item = Item(name, description)

    db.session().add(item)
    db.session().commit()

    message = "Esine luotiin onnistuneesti"
    return render_template("/item/newItem.html", form = NewItemForm(), message=message)
