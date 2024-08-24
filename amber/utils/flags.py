import os

def generate_flag():
    inner = os.urandom(32).hex()
    return "FLAG{" + inner + "}"
