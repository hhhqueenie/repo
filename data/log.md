# Data Sets
## Naming rules
+ **author name_book name.txt**
+ In `files` folder: there's a `info.xlsx`, used as a temporary statistics for foreign writers

## Text Checking (manual)
1. 删除译者序/前言
2. 简中
3. 后序/后言
4. 注释尽量都删了

## 需要添加的外国作家
+ 加缪：快乐的死 加缪手记
+ 阿西莫夫 重选
+ 尼采 拉康
+ 弗雷德里克·巴克曼： 一个叫欧维的男人决定去死/焦虑的人/熊镇/外婆的道歉信/清单人生
+ 菲利普·迪克 仿生人会梦见电子羊吗？
+ 中文：乐队/歌手（or 作词人？

## 改进
+ NER 加入分词dictionary - 感觉没必要 训练集怎么分的predict还会怎么分 不应该影响结果
+ build test set

# Front-end
1. Input page: 输入框再user friendly一些，加一个combo box for user to choose matching Foriegn or Chinese authors.
2. result page: 按照UI design美化，在结果下显示输入的原文(might add explainable AI in here by highlighting the sentences that influce classification decision the most)
3. size self adjustment: especially mobile
4. "关于" page: show the author lists contained in training setS

# Back-end
