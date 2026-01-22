from __future__ import annotations

from enum import Enum, auto
from typing import TYPE_CHECKING, TypeAlias, Union

if TYPE_CHECKING:
    from classes.diver import Diver
    from classes.treasure import Treasure

CellContent: TypeAlias = Union['Treasure', 'Diver', None]

class PlayerChoice(Enum):
    PICK = auto()
    THROW = auto()
    NOTHING = auto()
    CHANGE_DIRECTION = auto()
    ROLL_DICE = auto()