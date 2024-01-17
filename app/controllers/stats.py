from app import app
from flask_bcrypt import Bcrypt
from flask import render_template, request, flash, redirect, session
from app.models.stat import Stat
from app.decorators import login_required

#! READ
@app.route("/stats")
@login_required()
def get_all_stats(user):

  return render_template("dashboard.html", stats=Stat.get_all(), user = user)

#! READ
@app.route("/stat/<int:id>")
@login_required()
def get_one(user, id):

    return render_template("view_game.html", stat=Stat.get_by_id(id), user = user)

#! CREATE
@app.route("/stat")  # ? GET - <a> tags
@login_required()
def get_add_stat_form(user):
    return render_template("add_stat.html", user=user)
   

@app.route("/stat", methods=["POST"])  # ? POST - <form> tags
@login_required()
def add_stat(user):
    Stat.add_stats({
            "user_id": session["user_id"],
            "points": request.form["points"],
            "assists": request.form["assists"],
            "rebounds": request.form["rebounds"],
            "opponent": request.form["opponent"],
            "date": request.form["date"],
            
    })
    return redirect("/stats")  # redirect when data is updated


#! UPDATE
@app.route("/stat/update/<int:id>")  # ? GET - <a> tags
@login_required()
def update_stat_form(user, id):
    return render_template("update_stat.html", stat=Stat.get_by_id(id), user=user)


@app.route("/stat/update", methods=["POST"])  # ? POST - <form> tags
@login_required()
def update_stat(user):
    Stat.update_stats(
        {
            "id": request.form["id"],
            "user_id": session["user_id"],
            "points": request.form["points"],
            "assists": request.form["assists"],
            "rebounds": request.form["rebounds"],
            "opponent": request.form["opponent"],
            "date": request.form["date"],
        }
    )
    return redirect("/stats")  # redirect when data is updated


#! DELETE
@app.route("/stat/delete/<int:id>")
@login_required()
def delete(user, id):
  
    Stat.delete(id)
    flash("Stats deleted", "info")
    return redirect("/stats")


