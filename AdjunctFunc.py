#coding=utf-8
from __future__ import division
#__author__="Wang"
from osgeo import gdal
import numpy as np
import math
#确保除法返回真实的商

#获取点的地形元素类型
#首先设置不同地形元素（LandformsElements）的整数值
ZERON = 0; FLN = 1; PKN = 2; RIN = 3; SHN = 4; CVN = 5; SLN = 6; CNN = 7; FSN = 8; VLN = 9; PTN = 10; __N = 100; CNTN = 11
#然后构造一个检索表
Forms = np.array(
    #行数是正特征数目，列数是负特征数目
    [[FLN, FLN, FLN, FSN, FSN, VLN, VLN, VLN, PTN],
    [FLN, FLN, FSN, FSN, FSN, VLN, VLN, VLN, __N],
    [FLN, SHN, SLN, SLN, CNN, CNN, VLN, __N, __N],
    [SHN, SHN, SLN, SLN, SLN, CNN, __N, __N, __N],
    [SHN, SHN, CVN, SLN, SLN, __N, __N, __N, __N],
    [RIN, RIN, CVN, CVN, __N, __N, __N, __N, __N],
    [RIN, RIN, RIN, __N, __N, __N, __N, __N, __N],
    [RIN, RIN, __N, __N, __N, __N, __N, __N, __N],
    [PKN, __N, __N, __N, __N, __N, __N, __N, __N]]
)
def DetermineLE(NumPositives, NumNegatives):
    LandForm = Forms[NumPositives, NumNegatives]
    return LandForm

#获取各方向的一个特征点
def DPCalcOnetime(CalcPoints, firstpoint, lastpoint):
    maxDistance = 0
    FeaturePoint = 0
    k,b = ParaCalc(CalcPoints, firstpoint, lastpoint) #计算线参数
    #计算具有最远距离的特征点
    thispoint  = firstpoint #初始化每个计算点
    for i in range(firstpoint,lastpoint):
        distance = DisCalc(CalcPoints,thispoint,k,b)
        if (distance > maxDistance) :
            maxDistance = distance
            FeaturePoint = thispoint
        thispoint = thispoint + 1
    #返回特征点标号
    return FeaturePoint

#获取线参数
def ParaCalc(CalcPoints, firstpoint, lastpoint):
    k = (CalcPoints[lastpoint].elevation - CalcPoints[firstpoint].elevation)/(CalcPoints[lastpoint].distance - CalcPoints[firstpoint].distance)
    b = CalcPoints[firstpoint].elevation - k * CalcPoints[firstpoint].distance
    #print k,b
    return k,b

#计算每一点离直线的高差
def DisCalc(CalcPoints,thispoint,k,b):
    up = abs(CalcPoints[thispoint].elevation - (k * CalcPoints[thispoint].distance + b))
    down = math.sqrt(k*k + 1)
    distance = up/down
    return distance