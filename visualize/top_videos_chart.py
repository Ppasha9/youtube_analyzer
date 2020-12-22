import numpy as np
import matplotlib.pyplot as plt

from typing import List


def plot_top_videos_chart(top_videos_by_title: List):
    top_videos_by_title.sort(key=lambda top_video: top_video.trending_date)
    x = [top_video.trending_date for top_video in top_videos_by_title]
    y = [int(top_video.views) for top_video in top_videos_by_title]

    x_num = np.arange(len(x))

    plt.plot(x_num, y, '--k')
    plt.xticks(x_num, x)
    plt.ylabel("Количество просмотров")
    plt.xlabel("Дата")
    plt.title(f"Video '{top_videos_by_title[0].title}'")
    plt.show()
