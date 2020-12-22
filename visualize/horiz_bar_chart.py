import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import MaxNLocator


def plot_horiz_bar_chart(labels, sizes, xlabel, xmaxlim):
    fig, ax = plt.subplots()

    rects = ax.barh(
        np.arange(len(labels)),
        sizes,
        align="center",
        height=0.5,
        tick_label=labels,
        color=["red", "green", "blue", "forestgreen", "turquoise", "chocolate", "gold", "maroon", "navy",
               "orangered", "pink", "sienna", "violet", "yellowgreen", "indigo"])

    ax.set_xlim([0, xmaxlim])
    ax.xaxis.set_major_locator(MaxNLocator(24))
    ax.xaxis.grid(True, linestyle="--", which="major", color="grey", alpha=.25)

    ax.set_xlabel(xlabel)

    plt.legend(rects, sizes)

    plt.show()
