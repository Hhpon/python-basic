import os as os  # 处理文件和目录
from fnmatch import fnmatch
from cv2 import cv2
import pytesseract
from PIL import Image

img_suffix = '.jpg'
distance = 0
line_range = 1


def get_dynamic_binary_image(filedir, img_name):
    # 图片的自动二值化
    filename = 'charcode/out_img/' + \
        img_name.split('.')[0] + '-binary'+img_suffix
    img_name = filedir + '/' + img_name
    print(img_name)
    im = cv2.imread(img_name)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    # adaptiveThreshold 自动二值化的命令
    th1 = cv2.adaptiveThreshold(
        im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 1)
    cv2.imwrite(filename, th1)
    return th1


def clear_border(img, img_name):
    # 去除验证码里面的边框
    filename = 'charcode/out_img/' + \
        img_name.split('.')[0] + '-clearBorder'+img_suffix
    h, w = img.shape[:2]
    # 此处请注意，opencv转换的图片会旋转90°
    # 所以图片的高对应x轴
    for x in range(0, h):
        for y in range(0, w):
            # 此处的4是经验值，可以根据图片内容改变
            if y < distance or y > w - distance:
                img[x, y] = 255
            if x < distance or x > h - distance:
                img[x, y] = 255

    cv2.imwrite(filename, img)
    return img


def interference_line(img, img_name):
    # 线降噪
    filename = 'charcode/out_img/' + \
        img_name.split('.')[0]+'-interferenceline'+img_suffix
    h, w = img.shape[:2]
    # 此处请注意，opencv转换的图片会旋转90°
    # 所以图片的高对应x轴
    for y in range(line_range, w-line_range):
        for x in range(line_range, h-line_range):
            count = 0
            if img[x, y - line_range] > 245:
                count += 1
            if img[x, y + line_range] > 245:
                count += 1
            if img[x - line_range, y] > 245:
                count += 1
            if img[x + line_range, y] > 245:
                count += 1
            if count > 2:
                img[x, y] = 255
    cv2.imwrite(filename, img)
    return img


def interference_point(img, img_name, x=0, y=0):
    # 点降噪
    filename = 'charcode/out_img/' + \
        img_name.split('.')[0]+'-interferencepoint'+img_suffix
    h, w = img.shape[:2]
    cur_pixel = img[x, y]
    for y in range(0, w - 1):
        for x in range(0, h - 1):
            if y == 0:  # 第一行
                if x == 0:  # 左上顶点,4邻域
                    # 中心点旁边3个点
                    sum = int(cur_pixel) \
                        + int(img[x, y + 1]) \
                        + int(img[x + 1, y]) \
                        + int(img[x + 1, y + 1])
                    if sum <= 2 * 245:
                        img[x, y] = 0
                elif x == h - 1:  # 右上顶点
                    sum = int(cur_pixel) \
                        + int(img[x, y + 1]) \
                        + int(img[x - 1, y]) \
                        + int(img[x - 1, y + 1])
                    if sum <= 2 * 245:
                        img[x, y] = 0
                else:  # 最上非顶点,6邻域
                    sum = int(img[x - 1, y]) \
                        + int(img[x - 1, y + 1]) \
                        + int(cur_pixel) \
                        + int(img[x, y + 1]) \
                        + int(img[x + 1, y]) \
                        + int(img[x + 1, y + 1])
                    if sum <= 3 * 245:
                        img[x, y] = 0
            elif y == w - 1:  # 最下面一行
                if x == 0:  # 左下顶点
                    # 中心点旁边3个点
                    sum = int(cur_pixel) \
                        + int(img[x + 1, y]) \
                        + int(img[x + 1, y - 1]) \
                        + int(img[x, y - 1])
                    if sum <= 2 * 245:
                        img[x, y] = 0
                elif x == h - 1:  # 右下顶点
                    sum = int(cur_pixel) \
                        + int(img[x, y - 1]) \
                        + int(img[x - 1, y]) \
                        + int(img[x - 1, y - 1])

                    if sum <= 2 * 245:
                        img[x, y] = 0
                else:  # 最下非顶点,6邻域
                    sum = int(cur_pixel) \
                        + int(img[x - 1, y]) \
                        + int(img[x + 1, y]) \
                        + int(img[x, y - 1]) \
                        + int(img[x - 1, y - 1]) \
                        + int(img[x + 1, y - 1])
                    if sum <= 3 * 245:
                        img[x, y] = 0
            else:  # y不在边界
                if x == 0:  # 左边非顶点
                    sum = int(img[x, y - 1]) \
                        + int(cur_pixel) \
                        + int(img[x, y + 1]) \
                        + int(img[x + 1, y - 1]) \
                        + int(img[x + 1, y]) \
                        + int(img[x + 1, y + 1])

                    if sum <= 3 * 245:
                        img[x, y] = 0
                elif x == h - 1:  # 右边非顶点
                    sum = int(img[x, y - 1]) \
                        + int(cur_pixel) \
                        + int(img[x, y + 1]) \
                        + int(img[x - 1, y - 1]) \
                        + int(img[x - 1, y]) \
                        + int(img[x - 1, y + 1])

                    if sum <= 3 * 245:
                        img[x, y] = 0
                else:  # 具备9领域条件的
                    sum = int(img[x - 1, y - 1]) \
                        + int(img[x - 1, y]) \
                        + int(img[x - 1, y + 1]) \
                        + int(img[x, y - 1]) \
                        + int(cur_pixel) \
                        + int(img[x, y + 1]) \
                        + int(img[x + 1, y - 1]) \
                        + int(img[x + 1, y]) \
                        + int(img[x + 1, y + 1])
                    if sum <= 4 * 245:
                        img[x, y] = 0
    cv2.imwrite(filename, img)
    return img


if __name__ == "__main__":
    filedir = 'charcode/easy_img'

    for file in os.listdir(filedir):
        if fnmatch(file, '*'+img_suffix):

            # 自动二值化F
            im = get_dynamic_binary_image(filedir, file)

            # 去除“噪声”
            # 去除边框
            im = clear_border(im, file)
            # 线降噪
            im = interference_line(im, file)
            # 点降噪
            im = interference_point(im, file)

            print(pytesseract.image_to_string(im))
