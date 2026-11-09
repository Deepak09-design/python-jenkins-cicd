def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("Python Jenkins CI/CD Application")
    print("Addition:", add(10, 20))
    print("Subtraction:", subtract(20, 10))
    print("Multiplication:", multiply(5, 4))
    print("Division:", divide(20, 5))
