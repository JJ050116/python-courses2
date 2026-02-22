import cv2

img = cv2.imread('imgs/images.jpeg')

# find a center an image (height / 2, width / 2)
height, width = img.shape[:2]
center = (width // 2, height // 2)

# .getRotationMatrix2D() = 1.center 2. degree 3. sclae ratio
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)

# .warpAffine() = 1. img (input) 2. matrix 3. area (width, height)
img_rotated = cv2.warpAffine(img, matrix, (width, height))

cv2.imshow('Rotated', img_rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()