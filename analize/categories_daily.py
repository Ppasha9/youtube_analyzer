from pyspark.sql.types import StringType
from analize.utils import *

spark = get_session()
df = spark.read.format("mongo") \
    .option("uri", "mongodb://127.0.0.1/youtube.gb_videos") \
    .load()
categories = get_categories_dict(spark)

cd = df.groupBy(["date", "category_id"]).count().sort("date", ascending=False)
cd = cd.groupBy("category_id").agg(F.mean("count").alias("mean_daily")).sort("mean_daily", ascending=False)
cd = cd.withColumn("mean_daily_rate", cd.mean_daily / 200)
name_udf = F.udf(lambda c_id: categories[str(c_id)] if str(c_id) in categories else "unknown", StringType())
cd = cd.withColumn("category_named", name_udf(cd.category_id))
cd.show(truncate=False)
save_collection(cd, "categories_daily")
