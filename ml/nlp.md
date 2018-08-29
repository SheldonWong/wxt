
## 自然语言处理

### 自然语言处理的任务
[参考cips2016]

- 基础研究
    - 词法与句法分析
    - 语义分析
    - 篇章分析
    - 语言认知模型
    - 语言表示与深度学习
    - 知识图谱与计算
- 应用研究
    - 文本分类与聚类
    - 信息抽取
    - 情感分析
    - 自动文摘
    - 信息检索
    - 信息推荐与过滤
    - 自动问答
    - 机器翻译
    - 社会媒体处理
    - 语音技术
    - 文字识别
    - 多模态信息处理
    - 医疗健康信息处理
    - 少数民族信息处理

第一层面的词法分析（ lexical analysis）包括汉语分词和词性标注两部分。
第二个层面的句法分析（ syntactic parsing）是对输入的文本句子进行分析以得到句
子的句法结构的处理过程。
自然语言处理的第三个层面是语义分析（ semantic parsing）。语义分析的最终目的是
理解句子表达的真实语义。

### word2vec
- [paddlepaddle词向量](http://staging.paddlepaddle.org/documentation/docs/zh/0.14.0/new_docs/beginners_guide/basics/word2vec/index.html)
- [word2vec原理](https://www.cnblogs.com/pinard/p/7160330.html)
- [DeepLearning实战之word2vec](https://kexue.fm/usr/uploads/2017/04/146269300.pdf)
- [word2vec例子](https://www.zhihu.com/question/44832436)
- [getting-started-with-word2vec](https://textprocessing.org/getting-started-with-word2vec)

word2vec最大的应用是计算距离

### 工具篇
- [自然语言处理 中文分词 词性标注 命名实体识别 依存句法分析 关键词提取 新词发现 短语提取 自动摘要 文本分类 拼音简繁](https://github.com/hankcs/HanLP)

### fasttext
[fasttext源代码](https://heleifz.github.io/14732610572844.html)

```python
    def predict(self, texts, k=1):
        all_labels = []
        for text in texts:
            if text[-1] != '\n':
                text += '\n'
            labels = self._model.classifier_predict(text, k,
                    self.label_prefix, self.encoding)
            all_labels.append(labels)
        return all_labels

    def predict_proba(self, texts, k=1):
        results = []
        for text in texts:
            if text[-1] != '\n':
                text += '\n'
            result = self._model.classifier_predict_prob(text, k,
                    self.label_prefix, self.encoding)
            results.append(result)
        return results
```
从源码来看，给predict传参的时候，只需要传入一个text列表即可