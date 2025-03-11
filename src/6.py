import numpy as np

def get_random_code(length):
    """Generates a random string of letters and digits with the specified length.

    Args:
        length (int): The desired length of the string.

    Returns:
        str: A randomly generated string with the specified length.
    """
    letters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    code = ''
    for i in range(length):
        if i % 2 == 0:
            code += random.choice(letters)
        else:
            code += random.choice(numbers)
    return code