from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName('appName').setMaster('local')
sc = SparkContext(conf=conf)

spark = SparkSession(sc)


