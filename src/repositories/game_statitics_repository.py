from database_connection import database_connection


class GameStatitics:
    def __init__(self, db_name):
        self.db_connection = database_connection(db_name)

    def add_game_score(self, level, score):
        self.db_connection.execute("INSERT INTO Results (level, score) VALUES (?, ?)", [
            level.value, score])

    def get_best_score(self):
        top5 = self.db_connection.execute(
            "SELECT score, level From Results ORDER BY score LIMIT 5 ").fetchall()
        return top5
