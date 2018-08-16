## Bigdata

### 各种框架
监控与管理，存储，数据迁移，计算与分析，挖掘

存储分为分布式文件存储，NoSQL

计算分为离线计算，批计算，实时计算
离线计算，MapReduce与Spark的对比，其本质上都是把一个大的任务打散到各个机器分别执行，然后将各个机器的任务合并。
批计算，SQL，Hive，SparkSQl，Impala，Kylin这些框架的区别
实时计算，消息队列Kafka等，实时消息处理Storm，SparkStreaming，Flink

数据迁移,RDBMS->NoSQL,NoSQL->RDBMS

挖掘：二分类，多分类，回归，推荐等

- Ambari
基于Web的工具，用于配置，管理和监控Apache Hadoop集群，支持Hadoop HDFS，Hadoop MapReduce，Hive，HCatalog，HBase，ZooKeeper，Oozie，Pig和Sqoop。 Ambari还提供了一个用于查看群集运行状况的仪表板，例如热力图，以及可视化查看MapReduce，Pig和Hive应用程序的功能，以及以用户友好的方式诊断其性能特征的功能。
- Hadoop
	- HDFS
	- MapReduce
	- Yarn
- Hbase
- Hive
- Hue
- Impala
- Kylin
- Spark
	-Spark Core
	-Spark SQL
	-Spark Streaming
	-Spark Mlib
	-Spark X
- Kafka
- Storm
- Flink
- ElasticSearch
- Solr
- Sqoop
- DataX
- oozie
Oozie是一个用于管理Apache Hadoop作业的工作流程调度程序系统。Oozie Workflow作业是一个有向无环图（DAG）。Oozie Coordinator工作是由时间（频率）和数据可用性触发的经常性的Oozie Workflow工作。
Oozie与Hadoop堆栈的其余部分集成，支持多种类型的Hadoop作业（例如Java map-reduce，Streaming map-reduce，Pig，Hive，Sqoop和Distcp）以及系统特定的工作（例如 Java程序和shell脚本）。
- Tez
一个基于Hadoop YARN的通用数据流编程框架，它提供了一个强大而灵活的引擎来执行任意DAG任务，以处理批处理和交互式用例的数据。 Tez正被Hadoop生态系统中的Hive™，Pig™和其他框架以及其他商业软件（例如ETL工具）采用，以取代Hadoop™MapReduce作为底层执行引擎。
- ZooKeeper
	
- redis

### 工作流


### 对比
[MapReduce与Spark的对比]
[SQL on Hadoop的对比]
[消息队列的对比]
[实时计算框架对比storm，streaming，flink](https://bigdata.163yun.com/product/article/5)