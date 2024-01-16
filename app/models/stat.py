from app.config.mysqlconnection import connectToMySQL
from flask import session


class Stat:
    db = "bball_stats"

    def __init__(self, data):
        self.id = data["id"]
        self.user_id = data["user_id"]
        self.name = data["name"]
        self.points = data["points"]
        self.assists = data["assists"]
        self.rebounds = data["rebounds"]
        self.opponent = data["opponent"]
        self.date = data["date"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    #! READ
    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM stats WHERE stats.id = %(id)s"

        results = connectToMySQL(cls.db).query_db(query, {"id": id})

        return cls(results[0])
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM stats"

        results = connectToMySQL(cls.db).query_db(query, {"id": id})

        stats = []
        for stat in results:
            stats.append(cls(stat))

        return stats
    #! CREATE
    @classmethod
    def add_stats(cls, data):
        query = "INSERT INTO stats (user_id, name, points, assists, rebounds, opponent, date) VALUES (%(user_id)s, %(name)s, %(points)s, %(assists)s, %(rebounds)s, %(opponent)s, %(date)s)"

        return connectToMySQL(cls.db).query_db(query, data)
    
    #! DELETE
    @classmethod
    def delete(cls, id):
        query = "DELETE FROM stats WHERE stats.id = %(id)s"
        connectToMySQL(cls.db).query_db(query, {"id": id})

    #!UPDATE
    @classmethod
    def update_stats(cls, stat):
        query = "UPDATE stats SET name=%(name)s, points=%(points)s, assists=%(assists)s, rebounds=%(rebounds)s, opponent=%(opponent)s, date=%(date)s WHERE id = %(id)s"

        return connectToMySQL(cls.db).query_db(query, stat)
       