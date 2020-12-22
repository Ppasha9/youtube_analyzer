import numpy as np
import matplotlib.pyplot as plt


def plot_vert_bar_chart(labels, sizes, title, xlabel):
    fig, ax = plt.subplots()
    y_pos = np.arange(len(labels))
    ax.barh(y_pos, sizes, align="center", alpha=.5)
    ax.set_yticks(y_pos, labels)
    ax.set_xlabel(xlabel)

    sizes = [round(size, 3) for size in sizes]

    ax_right = ax.twinx()
    ax_right.set_yticks(y_pos)
    ax_right.set_ylim(ax.get_ylim())
    ax_right.set_yticklabels(sizes)
    ax_right.set_ylabel(xlabel)

    plt.title(title)
    plt.show()
