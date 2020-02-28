# from pyspark.sql import DataFrameReader
from pyspark.sql import *

spark = SparkSession\
  .builder\
  .appName("Dedomena")\
  .getOrCreate()

def make_spark_df(path_to_file):
    df = spark.read.csv(path_to_file)
    print (df) 
    print(df.show())

path = "/Users/samirmarin/workspaces/dedomena/example.csv" 
make_spark_df(path)

