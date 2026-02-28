import cv2

img = cv2.imread('imgs/images.jpeg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

saveFile = cv2.imwrite('GrayScale.jpeg', gray)
newFile = cv2.imread('GrayScale.jpeg')

cv2.imshow('Output', newFile)
cv2.waitKey(0)
cv2.destroyAllWindows()