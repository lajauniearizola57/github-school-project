import random

def get_random_code():
    # Generate a random 4-digit code
    return "".join(str(random.randint(0, 9)) for _ in range(4))

print(get_random_code())