# 使用generator打印杨辉三角形


def triangles():
    r = [1]
    while True:
        yield r
        r = [1] + [r[i]+r[i+1] for i in range(len(r)-1)] + [1]


index = 0
for n in triangles():
    if index == 10:
        break
    index += 1
    print(n)
o = triangles()
