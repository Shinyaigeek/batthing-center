def get_y(data, labels, label):
    idx = labels.index(label)
    return list(map(lambda col: col[idx], data))