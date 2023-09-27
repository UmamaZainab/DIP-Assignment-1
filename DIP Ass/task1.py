import cv2


image = cv2.imread('sample.jpg')

new_width = 256
new_height = 256
image_resized = cv2.resize(image, (new_width, new_height))

cv2.imwrite('resized_image.jpg', image_resized)
cv2.imshow('Resized Image', image_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
