from app.config.mysqlconnection import connectToMySQL
from flask import session


class Stat:
    db = "bball_stats"

    def __init__(self, data):
        self.id = data[""]
        self.user_id = data["user_id"]
        self.name = data["name"]
        self.points = data["points"]
        self.assists = data["assists"]
        self.rebounds = data["rebounds"]
        self.opponent = data["opponent"]
        self.date = data["date"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
       