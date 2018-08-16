[TOC]

## Python基础
### list
```python

```
### dict
- 树形字典打印
python默认字典输出是一行，不便于查看，我们可以使用json.dumps来使字典树形输出：

```python
#indent=1代表字节点比父节点前多几个空格
a = {}
print(json.dumps(a, indent=1))
```

### tuple


### set



### 文档与注释

zhushi.py

```python
class Shop:
    '''
    商品类所包含的属性及方法
    update改/更新
    find查找
    delete删除
    create添加
    '''

    def __init__(self):
        '''
        初始化商品的价格、日期、分类等
        '''
        pass

    def upDateIt(self):
        '''
        用来更新商品信息
        '''
        pass
```
print(help(zhushi))