import random
import re
from dataclasses import dataclass
from typing import List, Optional

DICE_RE = re.compile(r"^\s*(?:(\d+)\s*)?d\s*(\d+)\s*$", re.IGNORECASE)

@dataclass(frozen=True)
class WGResult:
    n: int
    sides: int
    rolls: List[int]
    successes: int
    sixes: int
    ones: int
    wrath: int

def parse_expr(expr: str) -> Optional[tuple[int, int]]:
    m = DICE_RE.match(expr or "")
    if not m:
        return None
    n_str, sides_str = m.groups()
    n = int(n_str) if n_str else 1
    sides = int(sides_str)
    return n, sides

def format_normal_die(value: int) -> str:
    if value == 6:
        return f"🟨**{value}**"
    if value == 1:
        return f"🟥**{value}**"
    if value >= 4:
        return f"🟩**{value}**"
    return f"🟦**{value}**"

def format_wrath_die(value: int) -> str:
    if value == 6:
        return f"☠**WRATH:🟨{value}** (Exalted)"
    if value == 1:
        return f"☠**WRATH:🟥{value}** (Complication)"
    if value >= 4:
        return f"☠**WRATH:🟩{value}**"
    return f"☠**WRATH:🟦{value}**"

def roll_wg(n: int) -> WGResult:
    # W&G: pool d6
    rolls = [random.randint(1, 6) for _ in range(n)]
    successes = sum(1 for r in rolls if r >= 4)
    sixes = sum(1 for r in rolls if r == 6)
    ones = sum(1 for r in rolls if r == 1)
    wrath = rolls[0]
    return WGResult(
        n=n,
        sides=6,
        rolls=rolls,
        successes=successes,
        sixes=sixes,
        ones=ones,
        wrath=wrath,
    )

def render_wg(result: WGResult) -> str:
    wrath = result.rolls[0]
    normals = result.rolls[1:]
    parts = [format_wrath_die(wrath)] + [format_normal_die(v) for v in normals]
    return "  ".join(parts)
