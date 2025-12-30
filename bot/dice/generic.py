import random
import re
from dataclasses import dataclass
from typing import List, Optional, Tuple

# Acepta:
#  - "d20"
#  - "2d8"
#  - "3d6+2"
#  - "4d10 - 1"
GENERIC_RE = re.compile(
    r"^\s*(?:(\d+)\s*)?d\s*(\d+)\s*(?:([+-])\s*(\d+))?\s*$",
    re.IGNORECASE
)

@dataclass(frozen=True)
class GenericRollResult:
    n: int
    sides: int
    modifier: int
    rolls: List[int]
    total: int

def parse_generic(expr: str) -> Optional[Tuple[int, int, int]]:
    m = GENERIC_RE.match(expr or "")
    if not m:
        return None

    n_str, sides_str, sign, mod_str = m.groups()
    n = int(n_str) if n_str else 1
    sides = int(sides_str)

    modifier = 0
    if sign and mod_str:
        modifier = int(mod_str)
        if sign == "-":
            modifier = -modifier

    return n, sides, modifier

def roll_generic(n: int, sides: int, modifier: int = 0) -> GenericRollResult:
    rolls = [random.randint(1, sides) for _ in range(n)]
    total = sum(rolls) + modifier
    return GenericRollResult(n=n, sides=sides, modifier=modifier, rolls=rolls, total=total)
