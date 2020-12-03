import numpy as np

def get_idx_top_k(arr, k):
    arr_np = np.array(arr);
    return arr_np.argsort()[:k]