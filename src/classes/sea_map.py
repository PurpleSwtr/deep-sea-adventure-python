from classes.treasure import Treasure
from presentation.ui_sea_map import print_sea_map_info
from classes.diver import Diver
from core.types import CellContent


class SeaMap():
    def __init__(self) -> None:
        self.treasures: list[CellContent] = []
    
    def init_start_treasures(self):
        # for tr in range(1,5):
        #     for i in range(8):
        #         new_tr = Treasure()
        #         new_tr.level = tr
        #         self.treasures.append(new_tr)
        for i, tr in enumerate(range(32)):
            new_tr = Treasure()
            new_tr.level = tr
            self.treasures.append(new_tr)

    def set_treasures(self, treasures: list[Treasure | None | Diver]):
        self.treasures = treasures

    # @staticmethod
    def display_map(self):
        sea_map = []
        for tr in self.treasures:
            if isinstance(tr, Treasure):
                sea_map.append(tr.level)
            elif isinstance(tr, Diver):
                sea_map.append(tr.icon)
            elif tr is None:
                sea_map.append(" ")
        print_sea_map_info(sea_map=sea_map)