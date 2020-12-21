import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import MaxNLocator


def plot_bar_chart(labels, sizes):
    fig, ax = plt.subplots()

    rects = ax.barh(
        np.arange(len(labels)),
        sizes,
        align="center",
        height=0.5,
        tick_label=labels,
        color=["red", "green", "blue", "forestgreen", "turquoise", "chocolate", "gold", "maroon", "navy",
               "orangered", "pink", "sienna", "violet", "yellowgreen", "indigo"])

    ax.set_xlim([0, 5.5])
    ax.xaxis.set_major_locator(MaxNLocator(24))
    ax.xaxis.grid(True, linestyle="--", which="major", color="grey", alpha=.25)

    ax.set_xlabel("Среднее количество дней в тренде")

    plt.legend(rects, sizes)

    plt.show()
