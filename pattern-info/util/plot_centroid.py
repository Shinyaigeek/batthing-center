def plot_centroid(arr, el, colors, plt):
    for i in range(len(arr)):
        col = arr[i]
        plt.scatter(col[int(el[0])], col[int(el[1])], c=colors[i], alpha=0.9, edgecolors=colors[i], marker="*")