import random
from classes.diver import Diver
from classes.sea_map import SeaMap
from classes.submarine import Submarine
from classes.treasure import Treasure

from core.types import PlayerChoice


class GameLogic():
    def __init__(self) -> None:
        self.round = 0
        self.sea_map = SeaMap() 
        self.submarine = Submarine()
        self.divers: list[Diver] = []
        self.active_diver: Diver

    def start_game(self):
        self.round = 1
        self.active_diver = random.choice(self.divers)

    def set_game_options(self, divers: list[Diver]):
        self.divers = divers
    
    @staticmethod
    def _roll_dice() -> tuple[int, int]:
        return (random.randint(1, 3), random.randint(1, 3))
    
    @staticmethod
    def get_length_turn(dices: tuple[int,int], diver: Diver):
        return sum(dices) - len(diver.treasures)
    
    @staticmethod
    def pick_up_treasure(diver: Diver, treasure: Treasure):
        diver.add_treasure(treasure=treasure)
        ...
    


    @staticmethod
    def player_choice(diver: Diver, choice: PlayerChoice):
        ...

    @staticmethod
    def turn_around(diver: Diver):
        if not diver.turned:
            # Важно сказать мол, это можно сделать только один раз и нельзя отменить!
            diver.turned = True
        else:
            # Говорим пользователю что нельзя развернутся дважды
            ...

    def process_choice_walk(self, diver: Diver, choice: PlayerChoice):
        match choice:
            case PlayerChoice.CHANGE_DIRECTION:
                self.turn_around(diver=diver)
                # Тут скорее всего запустим выбор ещё раз, но уже без выбора разворота
                ...
            case PlayerChoice.ROLL_DICE:
                # Бросаем кубики и ходим на нужное количество клекток
                dices = self._roll_dice()
                amount = self.get_length_turn(diver=diver, dices=dices)
                self.dive(diver=diver, amount=amount, direction_up=diver.turned)
                ...

    def process_choice_with_treasure(
            self, 
            diver: Diver, 
            choice: PlayerChoice, 
            step_to: int,
            
            ):
        match choice:
            case PlayerChoice.NOTHING:
                ...
            case PlayerChoice.PICK:
                treasure = self.sea_map.treasures.pop(step_to)
                if isinstance(treasure, Treasure):
                    diver.add_treasure(treasure=treasure)
                self.sea_map.treasures.insert(step_to, diver)
            case PlayerChoice.THROW:
                ...

        

    def dive(self, diver: Diver, amount: int, direction_up: bool):
        current_diver_position = diver.position
        if not direction_up:
            next_diver_position = current_diver_position + amount
        else:
            next_diver_position = current_diver_position - amount
        
        if next_diver_position != current_diver_position:
            treasure = self.sea_map.treasures[next_diver_position]
            if isinstance(treasure, Treasure):
                # TODO: логика выбора
                self.process_choice_with_treasure(diver=diver, choice=PlayerChoice.PICK, step_to=next_diver_position)
                ...
        
        ...