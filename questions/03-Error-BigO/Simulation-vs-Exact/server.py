import io
import random

import matplotlib.pyplot as plt
import numpy as np

def file(data):
    if data["filename"] == "figure.png":

        # create plt
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        npoints = 10
        n = np.linspace(0, 50, npoints)
        error = np.exp(5 - data["params"]["alpha"] * n)
        for i in range(npoints):
            error[i] = error[i] * random.choice([1.5, 0.5])
        plt.semilogy(n, error, "-")
        plt.grid()
        plt.xlabel("Running time (minutes)", fontsize=18)
        plt.ylabel("Error (degree Celsius)", fontsize=18)
        plt.autoscale(enable=True, tight=True)

        # Save the figure and return it as a buffer
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        return buf


def generate(data):

    error = 1
    c = 0
    while abs(np.log10(error) + c) < 1:
        alpha = np.random.rand() / 2 + 0.5
        c = random.choice([2, 4, 6])
        time = random.choices(population=[10, 20, 30], weights=[0.3, 0.5, 0.2], k=1)[0]
        error = np.exp(5 - time * alpha)

    if error >= 10 ** (-c):
        data["params"]["Aans"] = "true"
        data["params"]["Bans"] = "false"
    else:
        data["params"]["Aans"] = "false"
        data["params"]["Bans"] = "true"

    data["params"]["alpha"] = alpha
    data["params"]["c"] = c
    data["params"]["time"] = time