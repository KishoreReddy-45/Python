from pyspark.sql import SparkSession
from pyspark.sql.functions import sum as _sum

spark = SparkSession.builder.appName("Daily Sales Summary").getOrCreate()
df = spark.read.parquet("s3://sales-data/raw/")
agg_df = df.groupBy("sale_date").agg(_sum("amount").alias("total_sales"))
agg_df.write.mode("overwrite").parquet("s3://sales-data/summary/")
