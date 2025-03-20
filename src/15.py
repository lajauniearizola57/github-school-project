import random

def get_random_python_code():
    """Returns a random Python code snippet"""
    codes = [
        "print('Hello, World!')",
        "for i in range(10):\n\tprint(i)",
        "numbers = [1, 2, 3, 4, 5]\nsum = 0\nfor num in numbers:\nsum += num\nprint(sum)"
    ]
    return random.choice(codes)
