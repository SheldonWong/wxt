
#每一行都有详细的注释。主要是简单学会使用模型，并没有对特征过多分析。
import xlearn as xl
ffm_model = xl.create_ffm()
# 训练集
ffm_model.setTrain("./small_train.txt")
# 设置验证集
ffm_model.setValidate("./small_test.txt")

# 设置参数
param = {'task':'binary','lr':0.2,'lambda':0.002}

# 设置不同的评价指标
# 分类问题：acc(Accuracy);prec(precision);f1(f1 score);auc(AUC score)
param1 = {'task':'binary','lr':0.2,'lambda':0.002,'metric':'rmse'}
# 回归问题：mae,mape,rmsd(RMSE)
param2 = {'task':'binary','lr':0.2,'lambda':0.002, 'metric':'rmse'}

# 训练模型
ffm_model.fit(param, "model.out")

# 测试集
ffm_model.setTest("small_test.txt")
# 输出样本预测概率，范围(-1,1)
ffm_model.predict("model.out","output.txt")

# 设置预测概率范围为(0,1)
ffm_model.setSigmoid()
ffm_model.predict("model.out","output.txt")

# 转化为二分类(0,1)，没有阈值吗？？？
ffm_model.setSign()
ffm_model.predict("model.out","output.txt")

# 模型保存为txt格式，
ffm_model.setTXTModel("./model.txt")


