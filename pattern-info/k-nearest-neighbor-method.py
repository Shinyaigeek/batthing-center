from input.input import input_data_np
from leave_one_out.split import split
from util.get_distance import get_distance
from util.get_idx_top_k import get_idx_top_k

index_col = "species"
factors = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
max_k = 30

(data, index) = input_data_np("iris.csv", idx_col=index_col, factors=factors);

# パターン数
data_n = len(data)

(x_train_data, x_test_data) = split(data, 1);

def k_nearest_neighbor_method(x_train_data, x_test_data, y_train_data, k):
    distances = list(map(lambda x: get_distance(x, x_test_data), x_train_data))
    top_k_distances_idx = get_idx_top_k(distances, max_k)
    

for i in range(1):
    (x_train_data, x_test_data) = split(data, i);
    (y_train_data, y_test_data) = split(index, i);
    k_nearest_neighbor_method(x_train_data, x_test_data, y_train_data, max_k)

