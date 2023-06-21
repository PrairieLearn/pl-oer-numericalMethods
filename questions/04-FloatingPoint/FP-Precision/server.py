import random


def generate(data):
    a = random.randint(130, 200)
    data["params"]["a"] = a
    b = random.choice([5, 25, 125])
    data["params"]["b"] = b
    if b == 5:
        data["correct_answers"]["f"] = 8
    elif b == 25:
        data["correct_answers"]["f"] = 9
    elif b == 125:
        data["correct_answers"]["f"] = 10
    return data