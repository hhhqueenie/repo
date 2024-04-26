# Data Sets
## Naming rules
+ **author name_book name.txt**
+ list.csv: 
  + `Author`: author's Chinese name
  + `Author_Ori`: author's original/English name (for Chinese author: NaN)
  + `Word_Count`: word counting for data we have for this author
  + `Description`: short introduction for this author, for showing in the result page
+ In `files` folder: there's a `info.xlsx`, used as a temporary statistics for foreign writers

## Text Checking (manual)
1. 删除译者序/前言
2. 简中
3. 后序/后言
4. 注释尽量都删了

## 需要添加的外国作家
+ 道格拉斯·亚当斯_银河系漫游五部曲 不全
+ JK Rowling
+ 冰与火之歌
+ 阿西莫夫 重选
+ 解忧杂货铺


## 改进
+ NER 加入分词dictionary - 感觉没必要 训练集怎么分的predict还会怎么分 不应该影响结果
+ build test set

# Front-end
1. Input page: 输入框再user friendly一些，加一个combo box for user to choose matching Foriegn or Chinese authors.
2. result page: 按照UI design美化，在结果下显示输入的原文(might add explainable AI in here by highlighting the sentences that influce classification decision the most)
3. size self adjustment: especially mobile

# Back-end
