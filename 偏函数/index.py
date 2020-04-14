import functools

print(int('123', 8))


def int2(x, base=8):
    return int(x, base)

# 这个是一种方式，但是pyhton给我提供了另外一种简单的方法


int2_2 = functools.partial(int, base=2)


def foo(x, *args, **kw):
    print(x)
    print(args)
    print(kw)


foo(1, 2, 3, 4, 5, 6, a=1, b=2, c=3)
