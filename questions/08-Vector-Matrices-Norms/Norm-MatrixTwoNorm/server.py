import numpy as np
import numpy.linalg as la
import prairielearn as pl


def generate(data):

    M = np.random.randint(-100, 100, size=(3,)) / 10.0
    A = np.around(np.diag(M), 1)

    data["params"]["A"] = pl.to_json(A)
    data["correct_answers"]["two-norm"] = la.norm(A, 2)
    return data