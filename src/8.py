import random
import string

def generate_python_code():
    # Define a list of Python keywords
    keywords = ['if', 'else', 'for', 'while', 'def', 'class']
    
    # Generate a random keyword
    rand_keyword = random.choice(keywords)
    
    # Define a list of Python operators
    operators = ['+', '-', '/', '*', '%', '**', '//', '==', '<', '>', '>=', '<=']
    
    # Generate a random operator
    rand_operator = random.choice(operators)
    
    # Define a list of Python data types
    data_types = ['int', 'float', 'str', 'bool']
    
    # Generate a random data type
    rand_data_type = random.choice(data_types)
    
    # Define a list of Python variables
    variables = [f"x{i}" for i in range(10)]
    
    # Generate a random variable name
    rand_variable = random.choice(variables)
    
    # Generate a random number between 1 and 100
    rand_num = random.randint(1, 100)
    
    # Return the code
    return f"{rand_keyword} {rand_variable} {rand_operator} {rand_num}: print('Hello, world!')"