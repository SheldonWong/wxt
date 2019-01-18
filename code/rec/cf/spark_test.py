#from pyspark import SparkContext, SparkConf
from pyspark import SparkConf
from pyspark.sql import SparkSession

conf = SparkConf()
spark = SparkSession.builder.appName("cf").config(conf=conf).enableHiveSupport().getOrCreate()
sc = spark.sparkContext


data = [1, 2, 3, 4, 5]
distData = sc.parallelize(data)
print(distData)
