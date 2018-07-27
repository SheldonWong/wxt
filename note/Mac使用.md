#Mac使用笔记

## 写作平台
### 平台搭建,markdown

* 主要分为编辑和生成阶段，在编辑阶段完成md的书写，生成阶段生成带目录树的html，pdf等
* 安装sublime
* 安装ruby，gem，tocmd
* 安装node，npm，i5ting_toc，gitbook

```bash
brew update
brew install ruby
```
* 安装tocmd
```
gem install tocmd
```
* 使用tocmd生成左侧目录
```
sudo tocmd_local -f xx.md
```
或者
```
sudo tocmd -d .
```

### markdown编辑
* sublime-win,linux,mac
* markdown_plus-web
* Remarkable-linux

### 生成带左侧目录树的html或pdf
* gem- tocmd 
* npm- i5ting_toc -f Python.md
* npm- gitbook build . 

### 存在的问题
1. tocmd，i5ting_toc生成的目录树不够美观
2. tocmd生成的目录树靠下
3. gitbook生成的html页面左右翻页和head设置太显眼
4. gitbook权限不够

