from app import app
from flask_bcrypt import Bcrypt
from flask import render_template, request, flash, redirect, session
from app.models.stat import Stat



#! READ
@app.route("/stats")
def get_all_stats():

  if 'user_id' not in session:
    flash("You're not logged in!!")
    return redirect('/')

  
  return render_template("dashboard.html", stats=Stat.get_all())

#! READ
@app.route("/stat/<int:id>")
def get_one(id):
    return render_template("view_game.html", stat=Stat.get_by_id(id))

#! CREATE
@app.route("/stat")  # ? GET - <a> tags
def get_add_stat_form():
    if "user_id" in session:
        return render_template("add_stat.html")
    else:
        return redirect("/")


@app.route("/stat", methods=["POST"])  # ? POST - <form> tags
def add_stat():
    Stat.add_stats({
            "user_id": session["user_id"],
            "name": request.form["name"],
            "points": request.form["points"],
            "assists": request.form["assists"],
            "rebounds": request.form["rebounds"],
            "opponent": request.form["opponent"],
            "date": request.form["date"],
            
    })
    return redirect("/stats")  # redirect when data is updated


#! UPDATE
@app.route("/stat/update/<int:id>")  # ? GET - <a> tags
def update_stat_form(id):
    return render_template("update_stat.html", stat=Stat.get_by_id(id))


@app.route("/stat/update", methods=["POST"])  # ? POST - <form> tags
def update_stat():
    Stat.update_stats(
        {
            "user_id": session["user_id"],
            "name": request.form["name"],
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
def delete(id):
    Stat.delete(id)
    flash("Stats deleted", "info")
    return redirect("/stats")


