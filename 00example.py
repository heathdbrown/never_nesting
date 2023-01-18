# Original
def calculate(bottom: int, top: int) -> int:
    if top > bottom:
        total = 0
        for number in range(bottom, top):
            if number % 2 == 0:
                total += number
        return total
    else:
        return 0


if __name__ == "__main__":
    print(calculate(1, 10))
    print(calculate(6, 6))
