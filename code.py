from cv2 import cv2 as cv 

im = cv2.imread('code.jpeg')
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
