# -*- coding: utf-8 -*-

'a test module'

__author__ = 'hhpon'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello World')
    elif len(args) == 2:
        print('Hello,%s!' % args[1])
    else:
        print('too many arguments')

print(__name__)

if __name__ == '__main__':
    test()
