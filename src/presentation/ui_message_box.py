from utils.color_print import cprint


class MessageBox():
    def __init__(self) -> None:
        self.message: str = ""
        self.active: bool = True
    def update_message(self, message:str) -> None:
        self.message = message

    def print_message_box(self) -> None:
        if self.active:
            cprint(f"\n\n{"="*119}", fg="yellow")

            cprint(f"{" "*20}{self.message}", fg="yellow")

            cprint(f"{"="*119}", fg="yellow")
