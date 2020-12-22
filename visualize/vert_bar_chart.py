import numpy as np
import matplotlib.pyplot as plt


def plot_vert_bar_chart(labels, sizes, title, xlabel):
    y_pos = np.arange(len(labels))
    plt.barh(y_pos, sizes, align="center", alpha=.5)
    plt.yticks(y_pos, labels)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.show()
