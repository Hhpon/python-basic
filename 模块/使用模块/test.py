# 直接引入？
# python 也不含有private的属性
# 非常有用的代码封装和抽象的方法，即：
# 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。

import index

import greeting

print(greeting.greet('hhp'))
index.test()
