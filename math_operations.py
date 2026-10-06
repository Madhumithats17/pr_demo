def divide_numbers(a: float, b: float) -> float:
    # Potential bug: ZeroDivisionError not handled
    return a / b

def calculate_average(numbers: list) -> float:
    # Potential bug: Empty list causes ZeroDivisionError
    return sum(numbers) / len(numbers)

def greet_user(username: str) -> str:
    return f"Welcome back, {username}!"
