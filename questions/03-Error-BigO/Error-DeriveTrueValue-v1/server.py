import random


def generate(data):

    prompt_version_rand = random.randint(0, 3)
    prompt = None

    rel_error = random.randint(1, 20) / 100
    water_used = random.randint(4, 6) * 100 + random.randint(1, 8) * 10
    true_val = water_used / (1 - rel_error)

    prompt = (
        "Your friend made you Kool-Aid by diluting the mixture "
        + "in %d ml water. The amount of water she used was less than "
        + "suggested and has a relative error of %.2f.\n"
        + "What was the suggested amount in ml?"
    )
    prompt = prompt % (water_used, rel_error)

    data["params"]["prompt"] = prompt
    data["correct_answers"]["ans"] = true_val

    return data