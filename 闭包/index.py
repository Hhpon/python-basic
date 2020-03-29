def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


fun = lazy_sum(1, 2, 3, 4, 5)

print(fun())

# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
# 原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


fs1, fs2, fs3 = count()

print(fs1(), fs2(), fs3())


# def createCounter(i):
#     index = [0]

#     def counter():
#         index[0] = index[0]+1
#         return index[0]
#     return counter


# counterA = createCounter(0)
# print(counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
# print(counterA())

# def createCounter():
#     index = 0

#     def counter():
#         # python 无法获取上一层的变量
#         print(index)
#         index = index + 1
#         return index
#     return counter


# counterB = createCounter()
# print(counterB(), counterB(), counterB())
