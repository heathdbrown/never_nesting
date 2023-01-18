# Extraction and Inversion and reduction with expression and built-in
def is_even(number: int) -> int:
    if number % 2 != 0:
        return 0
    return number


def calculate(bottom: int, top: int) -> int:
    return sum(is_even(number) for number in range(bottom, top))


if __name__ == "__main__":
    print(calculate(1, 10))
    print(calculate(6, 6))
