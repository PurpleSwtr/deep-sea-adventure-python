import importlib

try:
    inquirer = importlib.import_module("InquirerPy.inquirer")
except ModuleNotFoundError as e:
    print(f"Модуль не найден: {e}")
    ...