import time
import requests
import json

url = 'https://wq.jd.com/commodity/comment/getcommentlist'
params = {
    "pagesize": 10,
    "sku": 100009082466,
    "page": 1
}
headers = {
    "Cookie": '__jdv=122270672|direct|-|none|-|1589974484095; __jdu=15899744840941786002848; shshshfpa=c1d8ff48-fb25-90fd-b101-4806a98f5d59-1589974484; areaId=10; ipLoc-djd=10-698-0-0; shshshfpb=vgv%2FEOycIxbF5Y0G%20p9Jcog%3D%3D; __jda=76161171.15899744840941786002848.1589974484.1589974484.1589982151.2; __jdc=76161171; PCSYCityID=CN_210000_210400_0; wxa_level=1; retina=1; webp=1; mba_muid=15899744840941786002848; visitkey=13148296642376651; sbx_hot_h=null; cid=9; __wga=1589982166754.1589982166754.1589982166754.1589982166754.1.1; PPRD_P=UUID.15899744840941786002848; sc_width=375; shshshfp=cd12062d29a98c6cec7f2916812321bf; shshshsID=464cd4dbddeb4f5991d9ef04b11af1c9_2_1589982167077; jxsid=15899821710256526551; wq_logid=1589982169.1420251312; wqmnx1=MDEyNjM5NToucjA2aTBlajk1c2UmZDZlZjJfNnNzc2EmODkzMnogIG4yTSBLLkxlcy4vYS5mZkJWQ1Uo; __jdb=76161171.4.15899744840941786002848|2.1589982151; mba_sid=15899821563616767047353448392.3',
    "User-Agent": 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    "Referer": 'https://item.m.jd.com/product/100009082466.html?price=699.00&fs=1&sceneval=2&jxsid=15899821710256526551&sid=&sf=newM&pos=1&csid=d03d6700fcb864c7416b6e4aff4b08f9_1589982164581_1_1589982164583&ss_symbol=8&ss_mtest=shop_entrance_t3,~&key=%E6%89%8B%E6%9C%BA'
}
data = requests.get(url, params=params, headers=headers)
print(type(data))
print(data.status_code)
f = open('test.txt', 'w')
f.write(data.text)
print(type(data.text))
json = json.loads(data.text)
print(json)
