import unittest
from entities.game_level import Level
from repositories.game_statitics_repository import GameStatitics
from database_initialize import initialize_database
import os


class Testrepository(unittest.TestCase):
    def test_create_repository(self):
        db_name = "test"
        initialize_database(db_name)
        gamestatitics = GameStatitics(db_name)
        gamestatitics.add_game_score(Level.EASY, 5)
        gamestatitics.add_game_score(Level.EASY, 10)
        gamestatitics.add_game_score(Level.HARD, 100)
        gamestatitics.add_game_score(Level.MEDIUM, 20)
        gamestatitics.add_game_score(Level.HARD, 30)
        gamestatitics.add_game_score(Level.HARD, 120)
        bestscore = gamestatitics.get_best_score()

        self.assertEqual(bestscore[0], (5, 1))
        self.assertEqual(bestscore[1], (10, 1))
        self.assertEqual(bestscore[2], (20, 2))
        self.assertEqual(bestscore[3], (30, 3))
        self.assertEqual(bestscore[4], (100, 3))
        self.assertEqual(len(bestscore), 5)
        os.remove("data/teststatistics.db")
