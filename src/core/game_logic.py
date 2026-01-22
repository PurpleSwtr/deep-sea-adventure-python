import random
import time
from classes.diver import Diver
from classes.sea_map import SeaMap
from classes.submarine import Submarine
from classes.treasure import Treasure

from core.types import CellContent, PlayerChoice
from presentation.ui_message_box import MessageBox
from presentation.ui_submarine import print_submarine_info

import os
clear = lambda: os.system('cls')

class GameLogic():
    def __init__(self) -> None:
        self.round = 0
        self.sea_map = SeaMap() 
        self.submarine = Submarine()
        self.divers: list[Diver] = []
        self.active_diver: Diver
        self.message_box: MessageBox = MessageBox()

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
        new_treasure = treasure
        diver.add_treasure(treasure=new_treasure)
        del(treasure)
        ...
    
    @staticmethod
    def player_choice(diver: Diver, choice: PlayerChoice):
        ...

    def turn_around(self, diver: Diver):
        if not diver.turned:
            # Важно сказать мол, это можно сделать только один раз и нельзя отменить!
            diver.turned = True
        else:
            # Говорим пользователю что нельзя развернутся дважды
            ...

    # TODO: По хорошему в отдельный класс вынести
    def display_interface(self):
        clear()
        print_submarine_info(oxygen=self.submarine.oxygen)
        self.sea_map.display_map()
        self.message_box.print_message_box()

    def process_choice_walk(self, diver: Diver, choice: PlayerChoice) -> CellContent:
        match choice:
            case PlayerChoice.CHANGE_DIRECTION:
                self.turn_around(diver=diver)
                # Тут скорее всего запустим выбор ещё раз, но уже без выбора разворота
                ...
            case PlayerChoice.ROLL_DICE:
                # Бросаем кубики и ходим на нужное количество клеток
                dices = self._roll_dice()
                self.message_box.update_message(f'Игрок {diver.name} выкинул {dices}')
                print(self.sea_map.treasures[diver.position])
                    
                self.display_interface()
                time.sleep(2)
                amount = self.get_length_turn(diver=diver, dices=dices)

                self.submarine.sub_oxygen(oxygen=len(diver.treasures))
                treasure = self.dive(diver=diver, amount=amount)
                return treasure
                ...

    def dive(self, diver: Diver, amount: int) -> CellContent:
        current_diver_position = diver.position
        if not diver.turned:
            next_diver_position = current_diver_position + amount
        else:
            next_diver_position = current_diver_position - amount
        
        if next_diver_position != current_diver_position:
            # TODO: Где-то тут нужно будет проврять срезом списка, не стоят ли игроки впереди которых можно перепрыгнуть

            treasure = self.sea_map.treasures[next_diver_position]
            
            self.sea_map.treasures[next_diver_position] = diver
            diver.position = next_diver_position
            return treasure
            # if isinstance(treasure, Treasure):
            #     # TODO: логика выбора


                
            #     self.process_choice_with_treasure(diver=diver, choice=PlayerChoice.PICK, treasure=treasure)
            #     ...
        
    def process_choice_with_treasure(
            self, 
            diver: Diver, 
            choice: PlayerChoice, 
            treasure: Treasure,
            ) -> PlayerChoice:
        match choice:
            case PlayerChoice.NOTHING:
                ...
            case PlayerChoice.PICK:
                if isinstance(treasure, Treasure):
                    diver.add_treasure(treasure=treasure)

                self.message_box.update_message("Вы подобрали сокровище!")
            case PlayerChoice.THROW:
                ...
        
        return choice