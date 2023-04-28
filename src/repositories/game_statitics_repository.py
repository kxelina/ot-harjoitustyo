class GameStatitics:
    def __init__(self, db_connection):
        self.connection = db_connection

    def add_game_score(self, level, score):
        print(f"level:{level}")
        self.connection.execute("INSERT INTO Results (level, score) VALUES (?, ?)", [
            level.value, score])

    def get_best_score(self):
        top5 = self.connection.execute(
            "SELECT score, level From Results ORDER BY score LIMIT 5 ").fetchall()
        return top5
