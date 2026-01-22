from presentation.ui_message_box import MessageBox

class UIManager():
    def __init__(self) -> None:
        self.message_box: MessageBox = MessageBox()
        self.active: bool = True
        
        self._submarine = None
        self._sea_map = None
        self._active_diver = None

    # def update_ui(self):

    # def set_game_objects(self, submarine: 'Submarine', sea_map: 'SeaMap', active_diver: 'Diver' = None):
    #     self._submarine = submarine
    #     self._sea_map = sea_map
    #     self._active_diver = active_diver