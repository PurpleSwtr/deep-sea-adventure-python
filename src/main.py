from classes.diver import Diver
from classes.treasure import Treasure
from core.game_logic import GameLogic
from presentation.ui_submarine import print_submarine_info
from presentation.ui_sea_map import print_sea_map_info
from presentation.ui_choice import display_player_choice
from core.config import player_choices_treasure, player_choices_walk

from classes.sea_map import SeaMap

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
    
    print_submarine_info(oxygen=25)
    gl.sea_map.display_map()
    # print_sea_map_info(sea_map=map)
    print()
    c_walk = display_player_choice(player_choices_walk)

    print(c_walk)

    gl.process_choice_walk(diver=diver, choice=c_walk)




    gl.sea_map.display_map()

    



if __name__ == "__main__":
    main()
