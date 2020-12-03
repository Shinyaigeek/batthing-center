def get_centroid(arr, labels, k, centroids):
    centroid = [0] * k;
    for i in range(k):
        init_centroid = [0] * len(arr[0])
        s = 0;
        for j in range(len(labels)):
            label = labels[j]
            if i == label:
                init_centroid += arr[j]
                s += 1
        if s == 0:
            centroid[i] = centroids[i]
        else:
            centroid[i] = list(map(lambda x: x / s, init_centroid));
    return centroid