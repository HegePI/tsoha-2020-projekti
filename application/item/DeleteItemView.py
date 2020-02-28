from application import app, db, bcrypt, login_required
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import current_user, logout_user
from application.item.ItemModel import Item

@app.route("/item/deleteItem/<int:id>", methods=["POST"])
@login_required(role="ANY")
def delete_item(id):
    item = Item.query.filter_by(id=id).first()
    db.session().delete(item)
    db.session.commit()

    message = "Esine poistettiin onnistuneesti"
    return render_template("item/showAllItems.html", message=message, items=Item.query.all())

@app.route("/item/deleteItemView/<int:id>", methods=["POST"])
@login_required(role="ANY")
def delete_item_view(id):
    return render_template("item/deleteItemView.html", item=Item.query.filter_by(id=id).first())