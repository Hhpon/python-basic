# 代码运行期间动态增加功能的方式，称之为“装饰器”
# $s = $func.__name__


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2020/4/7')


now()
