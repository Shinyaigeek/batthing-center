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
import matplotlib.pyplot as plt
from time import sleep


k = 2
colors = ["pink", "yellow", "blue", "green", "cyan"]
index_col = "species"
factors = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
plot_el = [1, 3]
repeat = 5
interval = 1

(data, _) = input_data_np("iris.csv", idx_col=index_col, factors=factors);

# パターン数
data_n = len(data)
init_labels = assign_random(data, k)

plot_scatter(data, init_labels, plot_el, colors, plt)

centroids = get_centroid(data, init_labels, k, [0] * k)

plot_centroid(centroids, plot_el, colors, plt)

labels = init_labels

plt.draw()

sleep(10)
plt.pause(10)

for _ in range(repeat):
    print("plot!!")
    labels = update_label(data, centroids, colors)
    plt.cla()
    plot_scatter(data, labels, plot_el, colors, plt)
    centroids = get_centroid(data, labels, k, centroids)
    plot_centroid(centroids, plot_el, colors, plt)
    plt.draw()
    sleep(interval)
    plt.pause(interval)



