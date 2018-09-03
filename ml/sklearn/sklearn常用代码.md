## sklearn常用代码


### 特征编码



### Pipeline
Pipeline 使用一系列 (key, value) 键值对来构建,其中 key 是你给这个步骤起的名字， value 是一个评估器对象:

```python
estimators = [('reduce_dim', PCA()), ('clf', SVC())]
pipe = Pipeline(estimators)

param_grid = dict(reduce_dim=[None, PCA(5), PCA(10)],
                   clf=[SVC(), LogisticRegression()],
                   clf__C=[0.1, 10, 100])
grid_search = GridSearchCV(pipe, param_grid=param_grid)
```
### GridSearch寻找最优参数
[参考](https://www.zybuluo.com/rianusr/note/1160802)
```python
parameters = {
	'n_neighbors':[5,10,15,20,30],
	'weights':['uniform','distance'],
	'p':[1,2]
}

knn = KNeighborsClassfier()
grid_search = GridSearchCV(knn,parameters,scoring='accuracy',cv=5)
grid_search.fit(x,y)
```


### 利用pipe和gridsearch寻找最优参数
```python
pipe = Pipeline([
    ('reduce_dim', PCA()),
    ('classify', LinearSVC())
])
N_FEATURES_OPTIONS = [2, 4, 8]
C_OPTIONS = [1, 10, 100, 1000]
param_grid = [
    {
        'reduce_dim': [PCA(iterated_power=7), NMF()],
        'reduce_dim__n_components': N_FEATURES_OPTIONS,
        'classify__C': C_OPTIONS
    },
    {
        'reduce_dim': [SelectKBest(chi2)],
        'reduce_dim__k': N_FEATURES_OPTIONS,
        'classify__C': C_OPTIONS
    },
]
grid = GridSearchCV(pipe, cv=3, n_jobs=1, param_grid=param_grid)

```