from classes.diver import Diver
from classes.treasure import Treasure
from core.game_logic import GameLogic
from presentation.ui_submarine import print_submarine_info
from presentation.ui_sea_map import print_sea_map_info
from presentation.ui_choice import display_player_choice
from core.config import player_choices_treasure, player_choices_walk

from classes.sea_map import SeaMap
from core.types import PlayerChoice

def main():
    tr = Treasure()
    tr.set_level(4)

    print(tr.get_points())

    gl = GameLogic()

    diver = Diver()
    # diver.add_treasure(treasure=tr)

    dices = gl._roll_dice()
    print(dices)
    print(gl.get_length_turn(dices=dices, diver=diver))
    

    gl.sea_map.init_start_treasures()
    # ==============================
    #           ПОДГОТОВКА
    # ==============================

    # print_submarine_info(oxygen=25)
    # gl.sea_map.display_map()
    # print_sea_map_info(sea_map=map)

    while True:
        gl.display_interface()

        print()
        c_walk = display_player_choice(player_choices_walk)

        print(c_walk)
        print()

        treasure = gl.process_choice_walk(diver=diver, choice=c_walk)

        choice_treasure = None


        if isinstance(treasure, Treasure):
            gl.message_box.update_message(f'На кону сокровище {treasure.level} ценности!')
            gl.display_interface()
            
            c_treasure = display_player_choice(player_choices_treasure)
            
            choice_treasure = gl.process_choice_with_treasure(diver=diver, choice=c_treasure, treasure=treasure)
            ...
        else:
            gl.message_box.update_message('Вы не нашли сокровищ')
        
        gl.sea_map.display_map()

        # if choice_treasure == PlayerChoice.PICK:
        #     gl.sea_map.treasures[diver.position] = None


    



if __name__ == "__main__":
    main()
