from application import app, db
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from application.adventure.AdventureModel import Adventure
from application.adventure.NewAdventureForm import NewAdventureForm


@app.route("/newAdventure")
@login_required
def new_adventure_form():
    return render_template("adventure/newAdventure.html", form = NewAdventureForm())


@app.route("/newAdventure", methods=["POST"])
@login_required
def create_new_adventure():

    form = NewAdventureForm(request.form)

    if not form.validate():
        return render_template("adventure/newAdventure.html", form=form)

    adventure_name = form.adventure_name.data

    adventure = Adventure.query.filter_by(adventure_name=adventure_name).first()

    if adventure != None:

        error = "Seikkailu kyseisellä nimellä on jo olemassa."
        return render_template("adventure/newAdventure.html", error=error, form=form)

    else:

        new_adventure = Adventure(adventure_name, 1, current_user.id)

        db.session().add(new_adventure)
        db.session().commit()

        message = "Uusi seikkailu luotiin onnistuneesti!"
        
        return render_template("menu/menu.html", message=message)