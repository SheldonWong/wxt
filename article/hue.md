
### 
1. 安装hue
git clone

2. make apps
安装过程遇到的问题，由于要需要某些权限，要用sudo 执行，sudo之后，用户环境切换为/etc/sudoers指定的环境，会出现mvn command not found的错误
解决方案，手动修改Makefile的安装路径到用户目录下，另外还顺便修改了下hadoop_home

3. 启动hue bin/hue runserver 或者 bin/supervisor

4. 配置组件

- 更换元数据库：https://www.cnblogs.com/ivanny/p/hue_mysql_meta_dabatase.html
```
[[database]]
engine=mysql
host=
port=<mysql端口，一般就是3306了>
user=<用户名>
password=<密码>
name=<数据库名称，新数据库，专门用于hue,里面现在没有任何表>
#初始化数据库
bin/hue syncdb
bin/hue migrate
```

- hadoop

core-site.xml
```
                <property>
                        <name>hadoop.proxyuser.hue.hosts</name>
                        <value>*</value>
                </property>

                <property>
                        <name>hadoop.proxyuser.hue.groups</name>
                        <value>*</value>
                </property>

```
hdfs.xml
```
                 <property>
                        <name>dfs.webhdfs.enabled</name>
                        <value>true</value>
                </property>

```

hue.ini
```
[hadoop]
  [[hdfs_clusters]]

    [[[default]]]
      fs_defaultfs=hdfs://localhost:9000
      webhdfs_url=http://localhost:50070/webhdfs/v1
      hadoop_conf_dir=

  [[yarn_clusters]]

    [[[default]]]
      resourcemanager_host=localhost
      resourcemanager_port=8032



```

- MySQL：

hue.ini
```
[[databases]]
    [[[mysql]]]
      nice_name="My SQL DB"
      name=hive
      engine=mysql
      host=localhost
      port=3306
      user=root
      password=root
```

- hive：

hive-site.xml
```
  <property>
  <name>hive.server2.enable.doAs</name>
  <value>false</value>
  </property>
```
hue.ini
```
[beeswax]
  hive_server_host=localhost
  hive_server_port=10000
  hive_conf_dir=/home/sheldonwong/app/apache-hive-2.3.3-bin/conf

```
启动hive服务    
bin/hiveserver2
