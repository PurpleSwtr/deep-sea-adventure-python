from core.config import config
import random

class Treasure():
    
    def __init__(self) -> None:
        self.level: int = 0
        self.points: int = 0
    
    def set_level(self, level: int):
        self.level = level

    def get_points(self):
        return random.randint(*config.LevelTreasureChances[self.level])
    
class PackTreasures(Treasure):
    def __init__(self) -> None:
        super().__init__()
        self.treasures: list[Treasure] = []

    def add_treasures(self, treasures: list[Treasure]):
        self.treasures.extend(treasures)

    def get_points(self):
        all_points = 0
        for tr in self.treasures:
            all_points += tr.get_points()
        return all_points