from pyspark.sql.types import StringType
from analize.utils import *

spark = get_session()
df = spark.read.format("mongo") \
    .option("uri", "mongodb://127.0.0.1/youtube.ru_videos") \
    .load()
categories = get_categories_dict(spark)
df = df \
    .withColumn("ratings_to_views", (df.likes + df.dislikes) / df.views) \
    .withColumn("likes_to_views", df.likes / df.views) \
    .withColumn("dislikes_to_views", df.dislikes / df.views) \
    .withColumn("likes_to_dislikes", df.likes / df.dislikes) \
    .withColumn("comments_to_views", df.comment_count / df.views)
cd = df.groupBy(["category_id"]).agg(
        F.mean("ratings_to_views").alias("ratings_to_views_mean"),
        F.mean("likes_to_views").alias("likes_to_views_mean"),
        F.mean("dislikes_to_views").alias("dislikes_to_views_mean"),
        F.mean("likes_to_dislikes").alias("likes_to_dislikes_mean"),
        F.mean("comments_to_views").alias("comments_to_views_mean"),
    )\
    .sort("ratings_to_views_mean", ascending=False)
name_udf = F.udf(lambda c_id: categories[str(c_id)] if str(c_id) in categories else "Nonprofits & Activism", StringType())
cd = cd.withColumn("category_named", name_udf(cd.category_id))
cd.show(truncate=False)
save_collection(cd, "categories_view_rating")
