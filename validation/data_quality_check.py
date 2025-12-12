from pyspark.sql.functions import col

def check_nulls(df, column):
    count = df.filter(col(column).isNull()).count()
    if count > 0:
        print(f"Column {column} has {count} null values")
    else:
        print(f"Column {column} has no nulls")

if __name__ == "__main__":
    from pyspark.sql import SparkSession
    spark = SparkSession.builder.appName("Data Quality").getOrCreate()
    df = spark.read.parquet("data.parquet")
    check_nulls(df, "customer_id")
