import datetime

from collections import namedtuple
from pymongo import MongoClient

from visualize.pie_chart import plot_pie_chart
from visualize.horiz_bar_chart import plot_horiz_bar_chart
from visualize.long_live_params_chart import plot_long_live_params_chart
from visualize.vert_bar_chart import plot_vert_bar_chart
from visualize.top_channels_chart import plot_top_channels_chart
from visualize.top_videos_chart import plot_top_videos_chart


TopVideo = namedtuple("TopVideo",
                      ["title", "publish_time", "trending_date", "views", "likes", "dislikes", "comment_count", "days_count"])


if __name__ == "__main__":
    mongo_client = MongoClient(host="localhost", port=27017)
    youtube_db = mongo_client["youtube"]

    # --- PIE CHART ---
    # categories_daily = youtube_db["categories_daily"]
    # all_categories_daily = list(categories_daily.find({}))
    #
    # labels_sizes = [(cat_daily["category_named"], round(cat_daily["mean_daily_rate"] * 100, 1)) for cat_daily in all_categories_daily]
    # labels_sizes.sort(key=lambda cat_daily: cat_daily[1], reverse=True)
    #
    # labels = list()
    # sizes = list()
    # for cat_daily in labels_sizes:
    #     labels.append(cat_daily[0])
    #     sizes.append(cat_daily[1])
    #
    # explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35)
    # plot_pie_chart(labels, sizes, explode)

    # --- BAR CHART ---
    # categories_long_live = youtube_db["categories_long_live"]
    # all_categories_long_live = list(categories_long_live.find({}))
    #
    # labels_params = [
    #     (elem["category_named"], round(elem["mean"], 2), elem["max"])
    #     for elem in all_categories_long_live]
    #
    # labels_params.sort(key=lambda elem: elem[1], reverse=True)
    #
    # labels_mean = list()
    # sizes_mean = list()
    # for cat_long_live in labels_params:
    #     labels_mean.append(cat_long_live[0])
    #     sizes_mean.append(cat_long_live[1])
    #
    # plot_horiz_bar_chart(labels_mean, sizes_mean, "Среднее количество дней в тренде", 1.5)
    #
    # labels_params.sort(key=lambda elem: elem[2], reverse=True)
    #
    # labels_max = list()
    # sizes_max = list()
    # for cat_long_live in labels_params:
    #     labels_max.append(cat_long_live[0])
    #     sizes_max.append(cat_long_live[2])
    #
    # plot_horiz_bar_chart(labels_max, sizes_max, "Максимальное количество дней в тренде", 5.5)

    # categories_long_live = youtube_db["categories_long_live"]
    # all_categories_long_live = list(categories_long_live.find({}))
    #
    # labels_params = [
    #     (elem["category_named"], round(elem["mean"], 3), elem["75%"], elem["90%"], elem["max"])
    #     for elem in all_categories_long_live]
    # labels_params.sort(key=lambda elem: elem[1], reverse=True)
    #
    # labels_params = labels_params[:5]
    #
    # labels = list()
    # params = list()
    # for elem in labels_params:
    #     labels.append(elem[0])
    #     params.append((elem[1], elem[2], elem[3], elem[4]))
    #
    # plot_long_live_params_chart(labels, params)

    # --- VERTICAL BAR CHARTS ---
    categories_view_rating = youtube_db["categories_view_rating"]
    all_categories_view_rating = list(categories_view_rating.find({}))

    for elem in all_categories_view_rating:
        if elem["category_named"] == "People & Blogs":
            all_categories_view_rating.remove(elem)
            break

    labels_means = [
        (elem["category_named"], elem["ratings_to_views_mean"], elem["likes_to_dislikes_mean"], elem["comments_to_views_mean"])
        for elem in all_categories_view_rating
    ]

    labels_means.sort(key=lambda elem: elem[1], reverse=True)
    labels_ratings = list()
    all_ratings_to_views_mean = list()
    for elem in labels_means:
        labels_ratings.append(elem[0])
        all_ratings_to_views_mean.append(elem[1])

    labels_means.sort(key=lambda elem: elem[2], reverse=True)
    labels_likes = list()
    all_likes_to_dislikes_mean = list()
    for elem in labels_means:
        labels_likes.append(elem[0])
        all_likes_to_dislikes_mean.append(elem[2])

    labels_means.sort(key=lambda elem: elem[3], reverse=True)
    labels_comments = list()
    all_comments_to_views_mean = list()
    for elem in labels_means:
        labels_comments.append(elem[0])
        all_comments_to_views_mean.append(elem[3])

    plot_vert_bar_chart(labels_ratings, all_ratings_to_views_mean, "Отношение между оцениванием видео и его просмотров",
                        "Количество оцениваний / количество просмотров")
    plot_vert_bar_chart(labels_likes, all_likes_to_dislikes_mean, "Отношение лайков к дизлайкам",
                        "Количество лайков / количество дизлайков")
    plot_vert_bar_chart(labels_comments, all_comments_to_views_mean, "Отношение комментируемости видео и его просматриваемости",
                        "Количество комментов / количество просмотр")

    # --- TOP CHANNELS ---
    # top_channels = youtube_db["top_channels"]
    # all_top_channels = top_channels.find({})
    #
    # titles_sizes = [
    #     (elem["channel_title"], elem["trend_days"], elem["trendable"])
    #     for elem in all_top_channels
    # ]
    #
    # titles_sizes.sort(key=lambda top_channel: top_channel[1], reverse=True)
    #
    # titles = list()
    # params = list()
    # for top_channel in titles_sizes:
    #     titles.append(top_channel[0])
    #     params.append((top_channel[1], top_channel[2]))

    # plot_top_channels_chart(titles, params)

    # --- REGRESSION ---
    # top_videos = youtube_db["top_videos"]
    # all_top_videos = top_videos.find({})
    #
    # def hack_date_str(date_str: str):
    #     if date_str.endswith(".1"):
    #         date_str += "1"
    #     return date_str
    #
    # def from_json_to_top_video(top_video):
    #     del top_video["_id"]
    #     top_video["trending_date"] = datetime.datetime.strptime("20" + top_video["trending_date"], "%Y.%d.%m").date()
    #     return TopVideo(**top_video)
    #
    # top_videos_structures = [from_json_to_top_video(top_video_json) for top_video_json in all_top_videos]
    # top_videos_by_titles = dict()
    # for top_video_struct in top_videos_structures:
    #     if top_video_struct.title in top_videos_by_titles.keys():
    #         top_videos_by_titles[top_video_struct.title].append(top_video_struct)
    #     else:
    #         top_videos_by_titles[top_video_struct.title] = [top_video_struct]
    #
    # plot_top_videos_chart(top_videos_by_titles["VERSUS #9 (сезон IV): Guf VS Птаха"])
    # plot_top_videos_chart(top_videos_by_titles["[BadComedian] - Движение Вверх (Плагиат или великая правда?)"])
