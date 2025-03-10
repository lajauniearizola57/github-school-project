import random

def get_random_string(length):
    """Returns a random string of length `length`."""
    letters = "abcdefghijklmnopqrstuvwxyz"
    return "".join(random.choice(letters) for _ in range(length))
