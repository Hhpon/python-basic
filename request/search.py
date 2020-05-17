import requests
import json
from download_img import download_img


def search_keyword(keyword):
    url = 'http://you.163.com/xhr/search/search.json'
    query = {
        'keyword': keyword,
        'page': 1
    }
    try:
        res = requests.get(url, params=query).json()
        results = res['data']['directly']['searcherResult']['result']
        product_id = []
        for result in results:
            product_id.append(result['id'])
            img_list = [result['listPicUrl'], result['scenePicUrl']]
            for imgUrl in img_list:
                download_img(imgUrl)
        return product_id
    except:
        raise


if __name__ == '__main__':
    search_keyword('文胸')
