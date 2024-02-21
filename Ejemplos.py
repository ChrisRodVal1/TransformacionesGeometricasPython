'''
#Redimensionalización

import numpy as np
import cv2
 
img = cv2.imread('pacman.png')
 
#Indicando el factor de escala
res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
 
# Indicando manualmente el nuevo tamaño deseado de la iamgen
height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)

cv2.imshow('img',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
#Traslación

import cv2
import numpy as np
 
img = cv2.imread('pacman.png',0)
rows,cols = img.shape
 
M = np.float32([[1,0,210],[0,1,20]])
dst = cv2.warpAffine(img,M,(cols,rows))
 
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
#Rotación

import cv2
import numpy as np

img = cv2.imread('pacman.png',0)
rows,cols = img.shape
 
M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
#Transformación Afín

import numpy as np
import matplotlib.pyplot as plt #carga la librería para graficar
import cv2
 
img = cv2.imread('pacman.png')
rows,cols,ch = img.shape
 
pts1 = np.float32([[100,400],[400,100],[100,100]])
pts2 = np.float32([[50,300],[400,200],[80,150]])
 
 
M = cv2.getAffineTransform(pts1,pts2)
dst = cv2.warpAffine(img,M,(cols,rows))
 
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
'''

'''
# Transformación de Perspectiva

import numpy as np
import matplotlib.pyplot as plt
import cv2
 
img = cv2.imread('pacman.png')
rows,cols,ch = img.shape
 
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
 
M = cv2.getPerspectiveTransform(pts1,pts2)
 
dst = cv2.warpPerspective(img,M,(300,300))
 
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
'''
