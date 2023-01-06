#coding=utf-8
#__author__="Wang"
from osgeo import gdal
import numpy as np

class Point:
    #该类是点结构体，以寻找各方向的特征点
    #This class is a point structure to find feature points in each direction
    direction = 0 #8方向的哪一个方向 # Which of the 8 directions
    col = 0
    row = 0
    angel = 0
    elevation = 0 #海拔高度 #Altitude
    height = 0 #相对中心点的高差 #Height difference relative to the center point
    distance = 0