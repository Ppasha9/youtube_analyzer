from pyspark.sql import SparkSession
import pyspark.sql.functions as F


def get_session():
    spark = SparkSession \
        .builder \
        .appName("analizer") \
        .getOrCreate()
    return spark


def get_categories_dict(spark):
    categories = spark.read.format("mongo") \
        .option("uri", "mongodb://127.0.0.1/youtube.us_categories") \
        .load()
    cs = categories.select(["id", "snippet.title"])
    cs_rdd = cs.rdd.map(lambda x: (x.id, x.title)).collect()
    categories = {}
    for pair in cs_rdd:
        categories[pair[0]] = pair[1]
    return categories


def save_collection(df, name):
    df.write \
        .format("mongo") \
        .mode("overwrite") \
        .option("uri", "mongodb://127.0.0.1/youtube") \
        .option("collection", name) \
        .save()


def groupby_apply_describe(df, groupby_col, stat_col):
    """From a grouby df object provide the stats
    of describe for each key in the groupby object.

    Parameters
    ----------
    df : spark dataframe groupby object
    col : column to compute statistics on

    """
    output = df.groupby(groupby_col).agg(
        F.count(stat_col).alias("count"),
        F.mean(stat_col).alias("mean"),
        F.stddev(stat_col).alias("std"),
        F.min(stat_col).alias("min"),
        F.expr(f"percentile({stat_col}, array(0.25))")[0].alias("%25"),
        F.expr(f"percentile({stat_col}, array(0.5))")[0].alias("%50"),
        F.expr(f"percentile({stat_col}, array(0.75))")[0].alias("%75"),
        F.max(stat_col).alias("max"),
    )
    return output
