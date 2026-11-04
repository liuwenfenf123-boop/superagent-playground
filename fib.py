"""Print the first 10 Fibonacci numbers, one per line (starting 0, 1, 1, 2, ...)."""


def fibonacci(count):
    """Return the first `count` Fibonacci numbers as a list."""
    numbers = []
    current, following = 0, 1
    for _ in range(count):
        numbers.append(current)
        current, following = following, current + following
    return numbers


if __name__ == "__main__":
    for number in fibonacci(10):
        print(number)
