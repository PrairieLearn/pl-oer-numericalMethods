import random


def generate(data):
    I_err = random.choice([4, 5, 6])
    R_err = random.choice([2, 3])

    data["params"]["I_err"] = I_err
    data["params"]["R_err"] = R_err

    data["params"]["correct"] = I_err + R_err
    data["params"]["wrong1"] = I_err
    data["params"]["wrong2"] = R_err
    data["params"]["wrong3"] = I_err * R_err

    return data