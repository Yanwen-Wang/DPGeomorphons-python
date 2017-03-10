from osgeo import gdal
import numpy as np

class TIFF:
	def __init__(self):
		self=self
	def __del__(self):
		pass
		
	def ReadTif(self,filename):
		dataset = gdal.Open(filename)
		im_width = dataset.RasterXSize
		im_height = dataset.RasterYSize
		im_bands = dataset.RasterCount
		print "Width:",im_width,",Height:",im_height,",Bands:",im_bands
		im_geotrans = dataset.GetGeoTransform()
		im_proj=dataset.GetProjection()
		im_data=dataset.ReadAsArray(0,0,im_width,im_height)
		type(im_data),im_data.shape
		del dataset
		print "READ Tiff is OK."
		return (im_data,im_geotrans,im_proj)
	
	def WriteTif(self,data,geotrans,proj,filename):
		if 'init8' in data.dtype.name:
			datatype = gdal.GDT_Byte
		elif 'init16' in data.dtype.name:
			datatype = gdal.GDT_UInt16
		else:
			datatype = gdal.GDT_Float64
		if len(data.shape)==3:
			bands,height,width=data.shape
		else:
			bands,(height,width)=1,data.shape
		driver=gdal.GetDriverByName("GTiff")
		dataset=driver.Create(filename,width,height,bands,datatype)
		dataset.SetGeoTransform(geotrans)
		dataset.SetProjection(proj)
		if bands==1:
			dataset.GetRasterBand(1).WriteArray(data)
		else:
			for i in range(bands):
				dataset.GetRasterBand(i+1).WriteArray(data[i])
		del dataset 
		print "Write Tiff is OK."