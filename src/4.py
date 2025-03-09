import random

def generate_random_python_code():
    # Generate a random number of lines
    num_lines = random.randint(1, 20)

    # Initialize an empty list to store the lines of code
    lines = []

    # Loop through the number of lines and generate a random line of Python code for each one
    for i in range(num_lines):
        # Generate a random number of tokens (words or symbols) per line
        num_tokens = random.randint(1, 20)

        # Initialize an empty list to store the tokens on this line
        line_tokens = []

        # Loop through the number of tokens and generate a random token for each one
        for j in range(num_tokens):
            # Choose a random type of token (string, integer, or symbol)
            token_type = random.choice(['string', 'integer', 'symbol'])

            if token_type == 'string':
                # Generate a random string token
                token = '"' + ' '.join(random.choice(['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']) for i in range(random.randint(5, 10))) + '"'
            elif token_type == 'integer':
                # Generate a random integer token
                token = str(random.randint(0, 100))
            else:
                # Generate a random symbol token
                token = random.choice(['+', '-', '*', '/', '%'])

            line_tokens.append(token)

        # Join the tokens on this line with spaces to form the full line of code
        lines.append(' '.join(line_tokens))

    # Return the list of lines as a single string of Python code
    return '\n'.join(lines)