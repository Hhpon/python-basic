# def odd():
#   print('1')
#   yield 1
#   print('3')
#   yield 3
#   print('5')
#   yield 5

# o = odd()

# next(o)

# next(o
# )

# next(o)


# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a+b
#         n = n + 1
#     return 'done'

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return 'done'


for n in fib(6):
    print(n)
