## 使用callgraph & SED & AWK完成静态语法分析  
(callgraph)[]是golang.org提供的函数调用的分析工具  

callgraph产生的结果包含了许多没有用的信息诸如……

所以就可以用awk&sed对结果处理，得到一份干净的调用依赖关系


## 常用的语句
1. 

