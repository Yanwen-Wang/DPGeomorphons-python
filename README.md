# DPGeomorphons
Geomorphons算法使用python实现，但是其中寻找特征点的方法并非使用“地形开放度”算法，而是使用“Douglas-Peucker”算法。   

----使用DP算法的原始Geomorphons算法----   
----王彦文，2017年3月10号----   

##重要文件    
###1. Geomorphons.py是主函数，含有算法入口。  
###2. MainFunc.py含有算法主体，AdjunctFunc.py含有算法中所用到的各个函数，TIFF.py包含读写栅格的函数。
###3. Point.py与Pattern.py分别抽象了运算中的点与地貌形态元素。

The Geomorphons algorithm is implemented in python, but the method of finding feature points is not the "terrain openness" algorithm, but the "Douglas-Peucker" algorithm.

----Original Geomorphons algorithm using DP algorithm----
----Wang Yanwen, March 10, 2017----

## important documents
###1. Geomorphons.py is the main function, which contains the algorithm entry.
###2. MainFunc.py contains the main body of the algorithm, AdjunctFunc.py contains the functions used in the algorithm, and TIFF.py contains the functions for reading and writing rasters.
###3. Point.py and Pattern.py respectively abstract the points and geomorphic elements in the operation.