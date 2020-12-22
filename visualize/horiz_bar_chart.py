import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import MaxNLocator


def plot_horiz_bar_chart(labels, sizes, xlabel, xmaxlim):
    fig, ax = plt.subplots()

    pos = np.arange(len(labels))

    rects = ax.barh(
        pos,
        sizes,
        align="center",
        height=0.5,
        tick_label=labels)

    ax.set_xlim([0, xmaxlim])
    ax.xaxis.set_major_locator(MaxNLocator(24))
    ax.xaxis.grid(True, linestyle="--", which="major", color="grey", alpha=.25)

    ax.set_xlabel(xlabel)

    ax_right = ax.twinx()
    ax_right.set_yticks(pos)
    ax_right.set_ylim(ax.get_ylim())
    ax_right.set_yticklabels(sizes)
    ax_right.set_ylabel(xlabel)

    # plt.legend(rects, sizes)

    plt.show()
