def createCounter():
    index = 0

    def counter():
        return index+1
    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
