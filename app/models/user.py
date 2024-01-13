from app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from app.models.stat import Stat



EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")


class User:
    db = "bball_stats"

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.stats = []

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM users LEFT JOIN stats ON stats.user_id = users.id WHERE users.id = %(id)s"

        results = connectToMySQL(cls.db).query_db(query, {"id": id})

        if not results:  # return if no results
            return None

        user = cls(results[0])

        for row in results:
            if row["stats.id"] is not None:  # check if child exists
                user.stats.append(
                    Stat(
                        {
                            "id": row["stats.id"],
                            "user_id": row["user_id"],
                            "name": row["name"],
                            "points": row["points"],
                            "assists": row["assists"],
                            "rebounds": row["rebounds"],
                            "opponent": row["opponent"],
                            "date": row["date"],
                            "created_at": row["stats.created_at"],
                            "updated_at": row["stats.updated_at"],
                        }
                    )
                )
        return user

    #! LOGIN
    @classmethod
    def get_by_email(cls, email):
        query = "SELECT * FROM users WHERE users.email = %(email)s"

        results = connectToMySQL(cls.db).query_db(query, {"email": email})

        if not results:
            return None

        return cls(results[0])

    #! CREATE
    @classmethod
    def create(cls, user):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"

        return connectToMySQL(cls.db).query_db(query, user)

    @staticmethod
    def validate_new_user(user):
        is_valid = True

        if not EMAIL_REGEX.match(user["email"]):
            flash("Invalid email address!")
            is_valid = False

        if len(user["first_name"]) < 3:
            flash("First Name must be at least 3 characters!!", "register")
            is_valid = False
        if len(user["last_name"]) < 3:
            flash("Last Name must be at least 3 characters!!", "register")
            is_valid = False
        if len(user["password"]) < 8:
            flash("First Name must be at least 8 characters.", "register")
            is_valid = False
        if user["password"] != user["confirm"]:
            flash("Passwords don't match!!", "register")
        return is_valid
