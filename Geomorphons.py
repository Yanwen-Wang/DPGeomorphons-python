#coding=utf-8
#__author__="Wang"
import MainFunc
import time

TimeStart = time.time()

DataFilename = "JIAOZUO_Clip_test.tif"
Radius = 20
MainFunc.CalcGeomporphons(DataFilename, Radius)

TimeEnd = time.time()
CalcTime = TimeEnd - TimeStart

print "程序运算：", CalcTime, "s"
