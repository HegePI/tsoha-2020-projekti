from application import app, db, bcrypt, login_required
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_bcrypt import Bcrypt
from flask_login import current_user
from application.item.ItemModel import Item
from sqlalchemy import exc 

@app.route("/allItems")
@login_required(role="ANY")
def list_all_items():
    return render_template("/item/showAllItems.html", items=Item.query.all())