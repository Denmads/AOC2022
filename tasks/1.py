def parse_input(data: str) -> list[list[int]]:
    elves = data.split("\n\n")
    parsed = list(map(lambda inv: list(map(lambda c: int(c), inv.split("\n"))), elves))
    return parsed

def run_a(data: str):
    inventories = parse_input(data)
    sums = sorted(map(lambda inv: sum(inv), inventories))
    print(f"Elves with most calories: {sums[-1]}")

def run_b(data: str):
    inventories = parse_input(data)
    sums = sorted(map(lambda inv: sum(inv), inventories))
    print(f"Sum of top three elves invetories: {sum(sums[-3:])}")