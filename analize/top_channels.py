from pyspark.sql.types import StringType
from analize.utils import *

spark = get_session()
df = spark.read.format("mongo") \
    .option("uri", "mongodb://127.0.0.1/youtube.ru_videos") \
    .load()

cd = df.groupBy(["channel_title"]).count().sort("count", ascending=False)
cd = cd.withColumnRenamed("count", "trend_days")
days = df.groupBy("trending_date").count().count()
cd = cd.withColumn("trendable", cd.trend_days / days).limit(15)
cd.show(truncate=False)
save_collection(cd, "top_channels")
