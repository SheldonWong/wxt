## 主成分分析
算法简介：
1. 求出各列的均值，然后用每一行减去均值
2. 求协方差矩阵
3. 求协方差矩阵的特征值，特征向量
4. 将特征值按照大小进行排序，取相应的前k个特征向量构成P
5. 降维，Y=PX


[理论](http://blog.codinglabs.org/articles/pca-tutorial.html)
[代码](https://applenob.github.io/pca.html)
[协方差计算](https://www.jianshu.com/p/aee3dbcc6fe6)