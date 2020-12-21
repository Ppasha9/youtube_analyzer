from pyspark.sql.functions import array, udf
from pyspark.sql.types import BooleanType, IntegerType, LongType
from analize.utils import *

spark = get_session()
df = spark.read.format("mongo") \
    .option("uri", "mongodb://127.0.0.1/youtube.gb_videos") \
    .load()

top = df.groupBy("title").count().sort("count", ascending=False).limit(10)
top = top.withColumnRenamed("count", "days_count")
cd_rdd = top.rdd.map(lambda x: (x.title, x.days_count)).collect()
top_titles = {}
for pair in cd_rdd:
    top_titles[pair[0]] = pair[1]
#print(top_titles)
cond_udf = udf(lambda title: title in top_titles.keys(), BooleanType())
cd = df.where(cond_udf(df.title)).select(["title", "date", "views", "likes", "dislikes", "comment_total"])
count_udf = udf(lambda title: top_titles[str(title)], IntegerType())
cd = cd.withColumn("days_count", count_udf(cd.title)).sort(["days_count", "views"], ascending=False)
cd.show(truncate=False)
save_collection(cd, "top_videos")
