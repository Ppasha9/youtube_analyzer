import numpy as np
import matplotlib.pyplot as plt


def plot_long_live_params_chart(labels, params):
    x_ticks = ["mean", "75%", "90%", "max"]
    x_ticks_nums = np.arange(len(x_ticks))

    colors = ["red", "blue", "green", "indigo", "gold"]

    bars = []
    for i in range(len(labels)):
        bars.append(plt.bar(x_ticks_nums, params[i], 0.15)[0])

    # for i in range(len(labels)):
    #     plt.bar(x_ticks_nums[0], params[i][0], 'o', color=colors[i], label=labels[i])
    #
    # for i in range(len(labels)):
    #     for j in range(1, 4):
    #         plt.bar(x_ticks_nums[j], params[i][j], 5, color=colors[i])

    plt.xticks(x_ticks_nums, x_ticks)
    plt.legend(bars, labels)

    plt.show()
