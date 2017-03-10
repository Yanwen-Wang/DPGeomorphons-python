#coding=utf-8
#__author__="Wang"
from osgeo import gdal
import numpy as np

class Point:
    #该类是点结构体，以寻找各方向的特征点
    direction = 0 #8方向的哪一个方向
    col = 0
    row = 0
    angel = 0
    elevation = 0 #海拔高度
    height = 0 #相对中心点的高差
    distance = 0