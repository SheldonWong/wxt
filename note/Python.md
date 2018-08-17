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

### pandas调整列顺序
```python
dict_a = {'user_id':['webbang','webbang','webbang'],'book_id':['3713327','4074636','26873486'],'rating':['4','4','4'],'mark_date':['2017-03-07','2017-03-07','2017-03-07']}

>>> df # 创建好的df列名默认按首字母顺序排序，和字典中的先后顺序并不一样，字典中是'user_id','book_id','rating','mark_date'
    book_id   mark_date rating  user_id
0   3713327  2017-03-07      4  webbang
1   4074636  2017-03-07      4  webbang
2  26873486  2017-03-07      4  webbang

>>> df = df[['user_id','book_id','rating','mark_date']] # 调整列顺序为'user_id','book_id','rating','mark_date'
>>> df
   user_id   book_id rating   mark_date
0  webbang   3713327      4  2017-03-07
1  webbang   4074636      4  2017-03-07
2  webbang  26873486      4  2017-03-07

```