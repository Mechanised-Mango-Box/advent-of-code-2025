
from typing import Tuple


UPPER = 100
INIT = 50


def shift(n: int, op: str) -> Tuple[int, int]:
    direction, steps = op[:1], int(op[1:])
    assert direction == "L" or direction == "R"
    match direction:
        case "L":
            sign = -1
        case "R":
            sign = 1

    loops, delta = divmod(steps, UPPER)

    next_n = n + (sign * delta)

    if n == 0 or 1 <= next_n <= 99:
        return loops, next_n % UPPER
    return loops + 1, next_n % UPPER


if __name__ == "__main__":
    dial: int = INIT
    pw: int = 0

    with open("./input", "r") as f:
        lines = f.readlines()
        for line in lines:
            op = line.strip()
            clicks, dial = shift(dial, op)
            pw += clicks
    print(pw)
