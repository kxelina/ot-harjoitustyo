from enum import Enum


class Level(Enum):
    """ Luokka, joka muttaa pelin tasot numeroksi """
    EASY = 1
    MEDIUM = 2
    HARD = 3

    def level_to_string(self):
        if self == Level.EASY:
            return "Easy"
        if self == Level.MEDIUM:
            return "Medium"
        return "Hard"
