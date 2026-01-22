from classes.treasure import Treasure

class Diver():
    def __init__(self) -> None:
        self.name: str = ""
        self.treasures: list[Treasure] = []
        self.victory_points: int = 0
        self.position: int = -1
        self.icon: str = "D"
        self.turned: bool = False

    def add_treasure(self, treasure: Treasure) -> None:
        self.treasures.append(treasure)


class DiverPlayer(Diver):
    ...

class DiverAI(Diver):
    ...