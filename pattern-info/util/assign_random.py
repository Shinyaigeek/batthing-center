import random

def assign_random(base, k):
    return list(map(lambda _: random.randint(0, k - 1), base))