from functools import reduce


def prod(list):
    def twoCount(x, y):
        return x * y

    return reduce(twoCount, list)


num = prod([3, 5, 7, 9])

print(num)

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
          '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2float(s):
    def str2int(n):
        return DIGITS[n]

    def str2float1(x, y):
        return x*10 + y
    index = s.index('.')

    def str2float2(x, y):
        return x*10 + y
    return reduce(str2float1, map(str2int, s[:index])) + reduce(str2float2, map(str2int, s[index+1:]))/10**len(s[index+1:])


num1 = str2float('123.456')

print(num1-123.456)
