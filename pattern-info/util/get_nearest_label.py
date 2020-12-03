def get_nearest_label(labels, nearest_labels):
    n_s = [0] * len(labels)
    for i in nearest_labels:
        idx = labels.index(i)
        n_s[idx] += 1
    max_value = max(n_s)
    return labels[n_s.index(max_value)]