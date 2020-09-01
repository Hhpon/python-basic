from pymongo import MongoClient
import pandas as pd
from pyecharts.charts import Bar, Pie
from pyecharts import options as opts
import re
from wordcloud import WordCloud
import jieba
from PIL import Image
import numpy as np

mongoClient = MongoClient('mongodb://localhost/')
netease = mongoClient['netease']
discuss = netease['discuss']

data = pd.DataFrame(list(discuss.find()))


skuinfo = data['skuInfo']

color = []
cup_size = []

for i in skuinfo.values.tolist():
    try:
        temp_cup = i[1].split(':')
        if temp_cup[0] == '杯码':
            temp_size = temp_cup[1]
            if '（' in temp_size:
                size = temp_size.split('（')[0]
                cup_size.append(size)
            else:
                cup_size.append(temp_size)
            temp_color = i[0].split(':')[1]
            color.append(temp_color)
    except:
        continue

df = pd.DataFrame(color, columns=['color'])
analyse_color = df['color'].value_counts()

bar = Bar()
bar.add_xaxis(analyse_color.index.values.tolist())
bar.add_yaxis("", analyse_color.values.tolist())
bar.set_global_opts(
    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30)),
    title_opts=opts.TitleOpts(title='颜色分布'),

)
bar.render('request/analyse/color-bar.html')

pie = Pie()
pie.add("", [list(z) for z in zip(analyse_color.index.values.tolist(
), analyse_color.values.tolist())], radius=['30%', '75%'], center=['50%', '50%'], rosetype='area')
pie.set_series_opts(label_opts=opts.LabelOpts(formatter='{b}:{d}%'))
pie.set_global_opts(title_opts=opts.TitleOpts(title='各颜色占比'),
                    legend_opts=opts.LegendOpts(type_="scroll", pos_left="80%", orient="vertical"))
pie.render('request/analyse/color-pie.html')

rege = r'\d'
cup_size_new = []
for i in cup_size:
    check = re.match(rege, i)
    if check:
        cup_size_new.append(i)
    else:
        tmp1 = i[0]
        tmp2 = i[1:]
        i = tmp2 + tmp1
        cup_size_new.append(i)
df2 = pd.DataFrame(cup_size_new, columns=['size'])
analyse_size = df2['size'].value_counts()

bar = Bar()
bar.add_xaxis(analyse_size.index.values.tolist())
bar.add_yaxis("", analyse_size.values.tolist())
bar.set_global_opts(
    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30)), title_opts=opts.TitleOpts(title='尺寸分布')
)
bar.render('request/analyse/size-bar.html')

# 星级分布
star = data['star'].value_counts()

# 评论词语
low_star_content = data[data['star'] == 5]['content']
stopworld = ('这', '那', '你', '我', '他', '她', '它')

font = 'request/FZNSTJW.TTF'


def gen_wordcloud(data, pic, world_pic):
    tmpstr = ''
    # print(data)
    for i in range(len(data) - 1):
        tmpstr += data[i]
    pseg = jieba.lcut(tmpstr)
    print(pseg)
    cut_word = ''
    for i in pseg:
        if i not in stopworld:
            cut_word += i
    img = Image.open(pic)
    img_array = np.array(img)
    wc = WordCloud(width=1800, height=1500,
                   background_color='white', font_path=font, mask=img_array)
    print(cut_word)
    wc.generate(cut_word)
    wc.to_file(world_pic)


gen_wordcloud(low_star_content.values.tolist(),
              'request/money.jpg', 'request/analyse/data_wc.png')
