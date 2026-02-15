import cv2

img = cv2.imread('imgs/images.jpeg')

if img is None:
    print('Cloud not found read the images.')

# gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('GrayScale', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()