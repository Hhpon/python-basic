# 使用generator打印杨辉三角形


def triangles():
    r = [1]
    while True:
        yield r
        r = [1] + [r[i]+r[i+1] for i in range(len(p)-1)] + [1]

