import math

def get_distance(x, y):
    init = 0;
    n = len(x);
    for i in range(n):
        init += math.pow(y[i] - x[i], 2)

    return math.sqrt(init)