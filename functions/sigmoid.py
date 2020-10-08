import numpy as np


def calculate_sigmoid(x):
    from time import sleep
    sleep(0.5)
    return 1/(1 + np.exp(-x))
