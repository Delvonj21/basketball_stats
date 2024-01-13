from app import app
from flask_bcrypt import Bcrypt
from flask import render_template, request, flash, redirect, session
from app.models.user import User
# from app.models.stat import Stat

bcrypt = Bcrypt(app)


@app.route("/")
def home():
    return render_template("home.html")


# #! READ
# @app.route("/user/pets/<int:id>")
# def get_user(id):
#     return render_template("user_pets.html", user=User.get_by_id(id))


#! REGISTER
@app.route("/user/register", methods=["POST"])
def user_register():
    if User.validate_new_user(request.form):
        User.create(
            {
                "first_name": request.form["first_name"],
                "last_name": request.form["last_name"],
                "email": request.form["email"],
                "password": bcrypt.generate_password_hash(request.form["password"]),
            }
        )
        flash("Thank you for registering", "register")

    return redirect("/")


#! LOGIN
@app.route("/user/login", methods=["POST"])
def user_login():
    email = request.form["email"]
    password = request.form["password"]
    
    found_user = User.get_by_email(email)
    if found_user and bcrypt.check_password_hash(found_user.password, password):
        session["user_id"] = found_user.id
        flash("Welcome Back")
        return redirect("/pets")

    flash("Invalid Credentials")
    return redirect("/")

#! LOGOUT
@app.route("/user/logout")
def user_logout():
    session.clear()
    return redirect("/")
