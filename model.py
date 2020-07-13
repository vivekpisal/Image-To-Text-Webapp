import cv2
#import easyocr
from pylab import rcParams
from IPython.display import Image
import pytesseract


rcParams['figure.figsize']=8,16

'''
def ImageToText(n):
	reader=easyocr.Reader(['en'])
	Image(n)
	op=reader.readtext(n)
	return op'''

def ImageToText(n):
	img=cv2.imread(n)
	op=pytesseract.image_to_string(img)
	return op