import requests
import time
from pymongo import MongoClient

mongoClient = MongoClient('mongodb://localhost/')
netease = mongoClient['netease']
discuss = netease['discuss']


def details(product_id):
    url = 'http://you.163.com/xhr/comment/listByItemByTag.json'
    try:
        product_list = []
        for i in range(1, 100):
            query = {
                "itemId": product_id,
                "page": i
            }
            res = requests.get(url, params=query).json()
            if not res['data']['commentList']:
                break
            print('爬取%s页评论' % i)
            commentList = res['data']['commentList']
            product_list.append(commentList)
            time.sleep(1)
            try:
                discuss.insert_many(commentList)
            except:
                continue
        return product_list
    except:
        raise

if __name__ == '__main__':
    details('3420029')