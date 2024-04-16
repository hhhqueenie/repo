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
3. 删除网站标签

## Utils:
1. word count (for checking data balance)
   + param: author's Chinese name
2. transform traditional Chinese to simplified Chinese
   + 主要还是需要手动check文章质量

## 需要添加的外国作家
+ 科幻
+ 悬疑 
  + 阿加莎
  + 柯南道尔
  + 钱德勒
+ JK Rowling

## Preprocess:
+ Replace `○` to be 零