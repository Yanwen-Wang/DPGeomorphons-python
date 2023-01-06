#coding=utf-8
#__author__="Wang"
from osgeo import gdal
import numpy as np
import Point

class Pattern:
    #该类是待推测点特征结构体
    #This class is the feature structure of the points to be inferred
    NumPositives = 0
    NumNegatives = 0
    positives = []
    negatives = []
    
    #8个方向特征（-1,0,1）的集合 
    # #A collection of 8 directional features (-1,0,1)
    pattern = [0,0,0,0,0,0,0,0] 

    # 8个方向特征点的集合，先初始化成8个元素的list 
    # A collection of 8 direction feature points, first initialized into a list of 8 elements
    featurePoint = [0,0,0,0,0,0,0,0] 
