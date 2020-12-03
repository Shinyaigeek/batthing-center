def get_datas(data, labels, target):
    init = [0] * len(data)
    for i in range(len(data)):
        col = [0] * len(target)
        has_hatena = True;
        for j in range(len(target)):
            idx = labels.index(target[j])
            if data[i][idx] == "?":
                has_hatena = False
            col[j] = data[i][idx]
        if has_hatena:
            init[i] = col
    return init

