
## 自然语言处理

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