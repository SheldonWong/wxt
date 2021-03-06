## 数据

### 数据集
[这是一份非常全面的开源数据集](https://www.jiqizhixin.com/articles/2018-09-05-2)

### 数据的类型
[参考](https://www.zybuluo.com/rianusr/note/1156011)
- 结构化数据
- 非结构化数据
	- 文本
	- 图片

### 认识数据
- 样本数，维度
- 特征，标签
- 特征取值范围，unique统计
- 数据分布


### 可视化


### 数据案例


### 人工特征工程
- 任务：原始的数据源，经过clean和transform，生成一个模型接受的input（特征向量，一般是数值类型的）
- transform
	- 原则上，尽可能多的从原始数据中挖掘有可能对结果产生影响的特征，去掉噪音（噪音如何理解，噪音可以是多方面的，例如原有的5列特征已经可以很好的划分数据，但是假如一列特征后，效果反而下降，再比如新增的一列特征其来源不可考，数据质量很低）。
	- 对于非结构化的数据-文本，可以采用one hot，bow，tfidf方法，将原始的文本transform成特征向量，或者采用Distributed Representation的方法，例如word2vec，将每个词映射成一个向量。
	- 对于非结构化的数据-图像，如果使用CNN等深度模型，可以直接将图像像素矩阵输入，深度学习会自动做特征工程。对于传统的机器学习方法，例如SVM，可以提取图像的关键特征，输入到SVM中。
	- 对于结构化的数据，可以做的事情包括，特征编码，特征组合，特征选择，特征降维等。
	- 由于计算机只能处理数值类型的数据，所以字符类型的数据需要被编码。
	- 由于有些数据特征有限，或者单个特征对结果影响不大，这个时候就可以尝试组合特征。例如<鹿晗，关晓彤>出现在一起时，会出现一个热点讨论。

- 思考：特征的区分度？特征与结果的因果关系？哪些特征会对结果产生影响？