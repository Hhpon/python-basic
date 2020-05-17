import requests

def download_img(imgUrl):
    res = requests.get(imgUrl, stream=True)
    if res.status_code == 200:
        urlSplitLists = imgUrl.split('/')
        name = urlSplitLists.pop()
        open('request/img/%s' % name,'wb').write(res.content)
    del res
