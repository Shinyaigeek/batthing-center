import numpy as np

def split(base, idx):
    index = np.ones(len(base), dtype=bool)
    index[idx] = False
    return (base[index], base[idx:idx + 1][0])