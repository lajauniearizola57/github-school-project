import random

def generate_random_python_code():
    # Define a list of possible Python statements
    statements = ["print('Hello, World!')", "x = 5", "y = 10", "z = x + y"]

    # Choose a random statement from the list
    chosen_statement = random.choice(statements)

    return chosen_statement
