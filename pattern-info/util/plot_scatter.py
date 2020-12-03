def plot_scatter(arr, labels, el, colors, plt):
    for i in range(len(arr)):
        col = arr[i]
        plt.scatter(col[int(el[0])], col[int(el[1])], c=colors[labels[i]], alpha=0.7, edgecolors=colors[labels[i]])
