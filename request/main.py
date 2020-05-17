from search import search_keyword
from details_page import details
import time


def main(keyword):
    product_id = search_keyword(keyword)
    print(product_id)
    for id in product_id:
        print("爬取产品 %s 信息" % id)
        details(id)


if __name__ == '__main__':
    print(__name__)
    main('文胸')
    print('name')
