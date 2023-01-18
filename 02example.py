# Inversion
def calculate(bottom: int, top: int) -> int:
    if bottom > top:
        return 0

    total = 0
    for number in range(bottom, top):
        if number % 2 == 0:
            total += number
    return total


if __name__ == "__main__":
    print(calculate(1, 10))
    print(calculate(6, 6))
