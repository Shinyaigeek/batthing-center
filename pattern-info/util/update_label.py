from .get_distance import get_distance

def update_label(arr, centroids, colors):
    labels = [-1] * len(arr)
    for i in range(len(arr)):
        col = arr[i]
        distance = 1000000000
        for c in range(len(centroids)):
            centroid = centroids[c]
            d = get_distance(centroid, col)
            if distance > d:
                distance = d
                labels[i] = c
    return labels