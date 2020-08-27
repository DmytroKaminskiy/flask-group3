import random
import string

def generate_random_password(password_len: int=10) -> str:
    chars = string.digits + \
            string.ascii_letters + \
            string.punctuation

    result = ''
    for _ in range(password_len):
        result += random.choice(chars)
    return result
