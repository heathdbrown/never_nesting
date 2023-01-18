# Extraction
def is_even(number: int) -> int:
    if number % 2 != 0:
        return 0
    return number


def calculate(bottom: int, top: int) -> int:
    if top > bottom:
        total = 0
        for number in range(bottom, top):
            total += is_even(number)
        return total
    else:
        return 0


if __name__ == "__main__":
    print(calculate(1, 10))
    print(calculate(6, 6))
