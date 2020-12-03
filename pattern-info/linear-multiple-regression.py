from input.input import input_data_np
from leave_one_out.split import split
from util.get_distance import get_distance
from util.get_idx_top_k import get_idx_top_k
from util.get_nearest_label import get_nearest_label
from util.assign_random import assign_random
from util.plot_scatter import plot_scatter
from util.plot_centroid import plot_centroid
from util.get_centroid import get_centroid
from util.update_label import update_label
from util.get_y import get_y
from util.get_datas import get_datas
import matplotlib.pyplot as plt
from time import sleep
import numpy as np

index_col = "car name"
factors = ["mpg", "cylinders", "displacement", "horsepower",
           "weight", "acceleration", "model year", "origin"]


(data, labels) = input_data_np("auto-mpg.csv", idx_col=index_col, factors=factors)
y_train_data = get_y(data, factors, "mpg")
x_train_data_1 = get_datas(data, factors, ["horsepower",
                                           "weight", ])
x_train_data_2 = get_datas(data, factors, ["cylinders", "displacement", "horsepower",
                                           "weight", "acceleration", "model year", "origin"])

x_train_data_1_np = np.array(x_train_data_1, dtype=float)
x_train_data_2_np = np.array(x_train_data_2, dtype=float)

w_1 = np.linalg.inv(x_train_data_1_np.T.dot(x_train_data_1_np)).dot(x_train_data_1_np.T).dot(y_train_data)
w_2 = np.linalg.inv(x_train_data_2_np.T.dot(x_train_data_2_np)).dot(x_train_data_2_np.T).dot(y_train_data)

print(w_1)
print(w_2)