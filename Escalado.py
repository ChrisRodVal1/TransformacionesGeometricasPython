import cv2
import numpy as np

# Load the image
image = cv2.imread('pacman.png')

# Define the scale factors for resizing
scale_x = 2.0  # Scale factor for width
scale_y = 2.0  # Scale factor for height

# Define the new dimensions for the scaled image
new_width = int(image.shape[1] * scale_x)
new_height = int(image.shape[0] * scale_y)

# Perform the scaling
scaled_image = cv2.resize(image, (new_width, new_height))

# Show the original and scaled images
cv2.imshow('Original', image)
cv2.imshow('Scaled', scaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
