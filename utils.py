import random
import string


def generate_password(length=15, letters=True, numbers=True, special_symbols=True):
    # Define the character set to use for generating the password
    chars = ''
    if letters:
        chars += string.ascii_letters
    if numbers:
        chars += string.digits
    if special_symbols:
        chars += string.punctuation

    # Generate a password by randomly selecting characters from the character set
    password = None
    if chars:
        password = ''.join(random.choice(chars) for _ in range(length))

    return password
