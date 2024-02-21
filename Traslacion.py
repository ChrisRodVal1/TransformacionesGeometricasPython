import cv2
import numpy as np

# Load the image
image = cv2.imread('pacman.png')

# Get the size of the image
height, width = image.shape[:2]

# Define the number of pixels to translate in the x and y directions
tx = 100  # Translation in the x direction
ty = 100  # Translation in the y direction

# Define the translation matrix
M = np.float32([[1, 0, tx], [0, 1, ty]])

# Apply the translation transformation to the image
translated_image = cv2.warpAffine(image, M, (width, height))

# Show the original image and the translated image
cv2.imshow('Original', image)
cv2.imshow('Translation', translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
