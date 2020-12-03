from input.input import input_data_np
from leave_one_out.split import split
from util.get_distance import get_distance
from util.get_idx_top_k import get_idx_top_k
from util.get_nearest_label import get_nearest_label
import matplotlib.pyplot as plt
import numpy as np

index_col = "species"
factors = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
labels = ["setosa", "virginica", "versicolor"]
max_k = 30

(data, index) = input_data_np("iris.csv", idx_col=index_col, factors=factors);
data = np.array(data)

# パターン数
data_n = len(data)

(x_train_data, x_test_data) = split(data, 1);

def k_nearest_neighbor_method(x_train_data, x_test_data, y_train_data, k):
    distances = list(map(lambda x: get_distance(x, x_test_data), x_train_data))
    top_k_distances_idx = get_idx_top_k(distances, k)
    nearest_labels = list(map(lambda idx: y_train_data[idx], top_k_distances_idx))
    predict_label = get_nearest_label(labels, nearest_labels)
    return predict_label

classed_correctly_rate = [0] * max_k

for k in range(1, max_k + 1):
    classed_correctly = 0
    for i in range(data_n):
        (x_train_data, x_test_data) = split(data, i);
        (y_train_data, y_test_data) = split(index, i);
        predict_label = k_nearest_neighbor_method(x_train_data, x_test_data, y_train_data, k)
        if predict_label == y_test_data:
            classed_correctly += 1
    classed_correctly_rate[k - 1] = classed_correctly / data_n * 100

for i in range(len(classed_correctly_rate)):
    print(str(i + 1) + ": " + str(classed_correctly_rate[i]) + "%")
plt.plot(range(1, max_k + 1), classed_correctly_rate)
plt.show()

