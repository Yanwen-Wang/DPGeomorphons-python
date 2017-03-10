#coding=utf-8
#__author__="Wang"
import numpy as np
from osgeo import ogr
import math
import TIFF
import AdjunctFunc as AF
from Pattern import * #如果要将Pattern类实例化，必须要用这种形式
from Point import *
from numpy import *
from copy import deepcopy #在实现点集的时候，此处需要深复制，因此引用deepcopy
from osgeo import ogr

''' 各示意图
directions
  3|2|1
  4|0|8
  5|6|7
  nextR = [-1, -1, -1, 0, 1, 1, 1, 0]  #行方向
  nextC = [1, 0, -1, -1, -1, 0, 1, 1]  #列方向
'''

def CalcGeomporphons(filename, Radius): #计算主函数
    #读入数据
    Tif_driver = TIFF.TIFF()
    Data, Geotrans, Proj = Tif_driver.ReadTif(filename)

    #规定8方向坐标
    nextR = [-1, -1, -1, 0, 1, 1, 1, 0]  #行方向
    nextC = [1, 0, -1, -1, -1, 0, 1, 1]  #列方向

    #数据总行列数，读取数据栅格大小
    RowNum = len(Data[:,1])
    ColNum = len(Data[1,:])
    CellSize = Geotrans[1]
    #初始化要存储地形元素的矩阵
    LndElmData = np.zeros((RowNum,ColNum))

    #设置特征阈值
    flat_distance = CellSize * 3 #为了避免窗口内起伏的误差，所有点将从3格之外开始计算
    flat_angel = 0.052 #设置角度阈值大小，此处数值为弧度值，设置为3°的弧度值
    #flat_height = CellSize *0.1 #设置高度阈值大小

    #step1：到达待处理点
    for i in range(Radius, RowNum - Radius):
        for j in range(Radius, ColNum - Radius):
            #初始化该点的8方向特征集合，初始化点集
            CalcPattern = Pattern()

            #step2：到达待处理点之后，要在待处理点的8个方向上找特征点
            for k in range(8):
                # 每个方向上的特征暂时为0
                CurPoint = Point() #待计算的边界点通过curPoint来实现
                CurPoint.direction = k
                CalcPoints = [] #初始化一个存储特征点集的list
                #CalcPointsToKeep = [] #初始化不同窗口大小下分别保留的特征点，此单尺度程序用不上

                #step3：确定了待处理点的处理方向后，在每个方向上存储点
                for m in range(4,Radius+1): #因为周围三个栅格不参与计算，所以从第4个开始，到最大半径（因为此处用range函数，所以最大值是Radius+1）。
                    CurPoint.row = i + m * nextR[k] #得到该方向此点的行坐标
                    CurPoint.col = j + m * nextC[k] #得到该方向此点的列坐标
                    CurPoint.elevation = Data[CurPoint.row, CurPoint.col]
                    CurPoint.height = CurPoint.elevation - Data[i,j]
                    CurPoint.distance = CellSize * math.sqrt(((CurPoint.col-j)*(CurPoint.col-j) +(CurPoint.row-i)*(CurPoint.row-i)))
                    CurPoint.angel = math.atan2(CurPoint.height,CurPoint.distance)
                    CurPointCopy = deepcopy(CurPoint) #如果直接append(CurPoint)，会因为浅复制而导致存储的都是最后一个点的信息，因此此处需要先深复制CurPoint的信息到CurPointCopy，再进行append
                    CalcPoints.append(CurPointCopy) #添加一个点

                #step4：在上一步存储的点里寻找特征点
                firstpoint = 0
                lastpoint = len(CalcPoints) - 1
                FeaturePoint = AF.DPCalcOnetime(CalcPoints, firstpoint, lastpoint)

                #step5：判断特征点与阈值关系，从而确定是1(postive)，0，-1(negative)关系
                if (CalcPoints[FeaturePoint].angel > flat_angel):
                    CalcPattern.positives.append(k)
                    CalcPattern.NumPositives = CalcPattern.NumPositives + 1
                    CalcPattern.pattern[k] = 1
                    CalcPattern.featurePoint[k] = CalcPoints[FeaturePoint]
                if (CalcPoints[FeaturePoint].angel < -flat_angel):
                    CalcPattern.negatives.append(k)
                    CalcPattern.NumNegatives = CalcPattern.NumNegatives + 1
                    CalcPattern.pattern[k] = -1
                    CalcPattern.featurePoint[k] = CalcPoints[FeaturePoint]

            #step6：确定每一个点的地形元素类型
            LndElmData[i,j] = AF.DetermineLE(CalcPattern.NumPositives, CalcPattern.NumNegatives)
            print LndElmData[i,j],"  ",i,"行",j,"列"

    #step7：将数据写入Tif并存储
    WriteFileName = "TestResult.tif"
    Tif_driver.WriteTif(LndElmData,Geotrans,Proj,WriteFileName)
    print "OK"
    #return ResultData