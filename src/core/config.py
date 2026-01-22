from core.types import PlayerChoice


player_choices_walk = {
    "Бросить кубики": PlayerChoice.ROLL_DICE,
    "Развернутся": PlayerChoice.CHANGE_DIRECTION,
}

player_choices_treasure = {
    "Взять сокровище": PlayerChoice.PICK,
    "Оставить своё сокровище": PlayerChoice.THROW,
    "Не брать сокровище": PlayerChoice.NOTHING,
}

class Config():
    def __init__(self) -> None:
        self.LevelTreasureChances = {
            1: (0,3),
            2: (4,7),
            3: (8,11),
            4: (12,15),
        }
        self.StartingTreasures: tuple = (8, 8, 8, 8)

config = Config()