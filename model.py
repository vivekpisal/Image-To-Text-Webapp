import cv2
import easyocr
from pylab import rcParams
from IPython.display import Image


rcParams['figure.figsize']=8,16


def ImageToText(n):
	reader=easyocr.Reader(['en'])
	Image(n)
	op=reader.readtext(n)
	return op