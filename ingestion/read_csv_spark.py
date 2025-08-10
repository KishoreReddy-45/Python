from pyspark.sql import SparkSession

def read_csv_from_s3(s3_path):
    spark = SparkSession.builder.appName("CSV Ingestion").getOrCreate()
    df = spark.read.csv(s3_path, header=True, inferSchema=True)
    return df

if __name__ == "__main__":
    df = read_csv_from_s3("s3://my-bucket/input/data.csv")
    df.show()
