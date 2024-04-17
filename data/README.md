## Naming rules
+ **author name_book name.txt**
+ list.csv: 
  + `Author`: author's Chinese name
  + `Author_Ori`: author's original/English name (for Chinese author: NaN)
  + `Word_Count`: word counting for data we have for this author
  + `Description`: short introduction for this author, for showing in the result page

## Text Checking (manual)
1. 删除译者序/前言
2. 简中
3. 删除网站标签 ctrl+f搜索w (utils里写了自动化，不用手动了)
4. 后序/后言
5. 注释尽量都删了
查到 东野圭吾

## Utils:
1. word count (for checking data balance)
   + param: author's Chinese name
2. transform traditional Chinese to simplified Chinese
   + 主要还是需要手动check文章质量

## 需要添加的外国作家
+ 道格拉斯·亚当斯_银河系漫游五部曲 不全
+ JK Rowling

## Preprocess:
+ Replace `○` to be 零
+ 数字全洗了
+ 第x章 全洗了
+ '[x]' 注释洗了
+ 转小写 删空格 www的删了