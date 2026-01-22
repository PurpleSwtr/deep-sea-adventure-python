
class Submarine():
    def __init__(self) -> None:
        self.oxygen: int = 25
    
    def sub_oxygen(self, oxygen: int) -> None:
        self.oxygen -= oxygen