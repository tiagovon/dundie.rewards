from random import sample
from string import ascii_letters, digits


def generate_simple_password(size=8):
    """Generate a simple random password"""
    password = sample(ascii_letters + digits, size)
    return "".join(password)
