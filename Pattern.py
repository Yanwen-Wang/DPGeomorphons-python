#coding=utf-8
#__author__="Wang"
from osgeo import gdal
import numpy as np
import Point

class Pattern:
    #该类是待推测点特征结构体
    NumPositives = 0
    NumNegatives = 0
    positives = []
    negatives = []
    pattern = [0,0,0,0,0,0,0,0] #8个方向特征（-1,0,1）的集合
    featurePoint = [0,0,0,0,0,0,0,0] #8个方向特征点的集合，先初始化成8个元素的list
