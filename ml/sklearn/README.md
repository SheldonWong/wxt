### sklearn


### 预处理
[特征编码](https://www.cnblogs.com/king-lps/p/7846414.html)
[数据预处理](http://sklearn.lzjqsdd.com/modules/preprocessing.html)


### 模型

### 分类OVO，OVR，MVM
[机器学习：逻辑回归	OvR与OvO](http://www.cnblogs.com/volcao/p/9389921.html)
[多分类学习](https://zhuanlan.zhihu.com/p/31458945)


### SVM
[LinearSVC与SVC区别](https://www.jianshu.com/p/a817b94c43dd)
```
LinearSVC() 与 SVC(kernel='linear') 的区别概括如下：

LinearSVC() 最小化 hinge loss的平方，
SVC(kernel='linear') 最小化 hinge loss；
LinearSVC() 使用 one-vs-rest 处理多类问题，
SVC(kernel='linear') 使用 one-vs-one 处理多类问题；
LinearSVC() 使用linear执行，
SVC(kernel='linear')使用libsvm执行；
LinearSVC() 可以选择正则项和损失函数，
SVC(kernel='linear')使用默认设置。
```

### 决策树
[可视化决策树之Python实现](https://blog.csdn.net/llh_1178/article/details/78516774)

### Ensemble
[xgb参数]
[Python xgboost.XGBClassifier() Examples](https://www.programcreek.com/python/example/99824/xgboost.XGBClassifier)
[sklearn中的xgbc和xgb.train的区别](https://blog.csdn.net/liulina603/article/details/78771738)
[xgb的输入](https://blog.csdn.net/zc02051126/article/details/46771793)
[xgb调参](https://segmentfault.com/a/1190000014040317)
[xgb模型保存](https://stackoverflow.com/questions/43691380/how-to-save-load-xgboost-model)

### 模型评估
[模型评估](http://d0evi1.com/sklearn/model_evaluation/)

- classification_report中的support是什么意思？
[参考](http://sofasofa.io/forum_main_post.php?postid=1001384)
```
sklearn官方文档的解释是“The support is the number of occurrences of each class in y_true.”

class I的suppport是k，意思就是说该测试集中有k个样本的真实分类为class i.

所以你上面的表格里class 0 support = 1就是说，测试集里有1个样本的真实标签是class 0.

class 1 support = 1就是说，测试集里有1个样本的真实标签是class 1.

class 2 support = 3就是说，测试集里有3个样本的真实标签是class 2.
```