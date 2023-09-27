import cv2

image = cv2.imread('sample.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)




ret, binary_image = cv2.threshold(gray_image, 128 , 255, cv2.THRESH_BINARY)


cv2.imwrite('binary_output.jpg', binary_image)

cv2.imshow('Binary Image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
