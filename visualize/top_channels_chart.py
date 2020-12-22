import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import MaxNLocator


def plot_top_channels_chart(labels, params):
    fig, ax = plt.subplots()

    trendable_params = list()
    trend_days_params = list()
    for param in params:
        trend_days_params.append(str(param[0]))
        trendable_params.append(param[1])

    pos = np.arange(len(labels))
    rects = ax.barh(
        pos,
        trendable_params,
        align="center",
        height=0.5,
        tick_label=labels)

    ax.set_xlim([0, 1])
    ax.xaxis.set_major_locator(MaxNLocator(10))
    ax.xaxis.grid(True, linestyle="--", which="major", color="grey", alpha=.25)

    ax.set_xlabel("На сколько популярен канал (отношение количества дней в тренде к общему количеству дней")

    ax_right = ax.twinx()
    ax_right.set_yticks(pos)
    ax_right.set_ylim(ax.get_ylim())
    ax_right.set_yticklabels(trend_days_params)
    ax_right.set_ylabel('Количество дней в тренде')

    plt.show()

