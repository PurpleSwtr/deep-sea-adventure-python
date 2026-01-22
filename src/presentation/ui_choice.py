from dependencies import inquirer
from core.types import PlayerChoice

def choice(choices: list) -> str:
    result = inquirer.checkbox(
        message="Выберите действие:",
        choices=choices,
        validate=lambda x: len(x) == 1,
    ).execute()
    return result[0]

def display_player_choice(choices: dict) -> PlayerChoice:
    choices_displayed = list(choices.keys())
    user_choice = choice(choices=choices_displayed)
    return choices[user_choice]