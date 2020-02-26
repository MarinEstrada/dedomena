# from pyspark.sql import DataFrameReader
from pyspark.sql import *

spark = SparkSession\
  .builder\
  .appName("Dedomena")\
  .getOrCreate()

def make_spark_df(path_to_file):
	df = spark.read.csv(path_to_file)
	print (df)

make_spark_df("/drives/c/Users/adria/cmpt/bro_workfolder/dedomena/test.csv")

