def generate_random_code():
    # Generate a random integer between 1 and 100
    number = random.randint(1, 100)
    # Use the modulo operator to determine whether the number is even or odd
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
