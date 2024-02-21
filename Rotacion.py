import cv2
import numpy as np

# Load the image
image = cv2.imread('pacman.png')

# Get the size of the image
height, width = image.shape[:2]

# Define the angle of rotation
angle = 90

# Calculate the center of the image
center = (width // 2, height // 2)

# Define the rotation matrix
M = cv2.getRotationMatrix2D(center, angle, 1.0)

# Apply the rotation transformation to the image
rotated_image = cv2.warpAffine(image, M, (width, height))

# Show the original image and the rotated image
cv2.imshow('Original', image)
cv2.imshow('Rotation', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
