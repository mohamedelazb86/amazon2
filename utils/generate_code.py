import random

def generate_code(length=8):
    data='0123456789ABCDEFGHIJKLMNOPQWXYZST'
    code=''.join(random.choice(data) for x in range(length))
    return code