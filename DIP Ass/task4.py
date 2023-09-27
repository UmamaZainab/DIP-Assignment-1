import cv2
import numpy as np
import matplotlib.pyplot as plt

input_image = cv2.imread('image.jpg')

# Converting the image to grayscale
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap='gray')

# Applying Gaussian blur to the grayscale image
blurred_image = cv2.GaussianBlur(gray_image, (11, 11), 0)
plt.imshow(blurred_image, cmap='gray')

# Applying Canny edge detection to the blurred image
edges = cv2.Canny(blurred_image, 30, 150, 3)
plt.imshow(edges, cmap='gray')

# Dilating the detected edges
dilated_edges = cv2.dilate(edges, (1, 1), iterations=2)
plt.imshow(dilated_edges, cmap='gray')

(contours, hierarchy) = cv2.findContours(dilated_edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Creating an RGB version of the input image for visualization
rgb_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)

cv2.drawContours(rgb_image, contours, -1, (0, 255, 0), 2)
plt.imshow(rgb_image)

num_coins = len(contours)
print('Total coins in the image: ', num_coins)
plt.show()
