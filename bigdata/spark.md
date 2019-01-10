
## Spark提交与执行

- 提交带依赖的文件
- spark-submit --master yarn-cluster my_script.py --py-files my_dependency.zip
- https://stackoverflow.com/questions/35214231/importerror-no-module-named-numpy-on-spark-workers

## SparkSql
- 创建df



## SparkRDD
### 创建RDD
```python
lines = sc.textFile("/path/to/README.md")
```

### RDD计算

### RDD存储

### RDD编程经验
1. case

2. 结果存储
/tmp/ 保存时间


## Spark写Redis

[('a',1),()]