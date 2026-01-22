
class Submarine():
    def __init__(self) -> None:
        self.oxygen: int = 20
    
    def sub_oxygen(self, oxygen: int) -> None:
        self.oxygen -= oxygen