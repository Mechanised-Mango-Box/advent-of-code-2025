
UPPER = 100
INIT = 50


def shift(n: int, op: str):
    direction, steps = op[:1], int(op[1:])
    assert direction == "L" or direction == "R"

    match direction:
        case "L":
            sign = -1
        case "R":
            sign = 1

    return (n + (sign * steps) + UPPER) % UPPER


if __name__ == "__main__":
    dial: int = INIT
    pw: int = 0

    with open("./input", "r") as f:
        lines = f.readlines()
        for line in lines:
            op = line.strip()
            dial = shift(dial, op)
            pw += dial == 0
    print(pw)
