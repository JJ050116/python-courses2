import cv2

img = cv2.imread('imgs/images.jpeg')

# width / 2
# height / 2

height, width = img.shape[:2]
center = (width//2, height//2)

# .getRotationMatrix2D() = 1. center (formula center) 2. degree 3. scale
angle = cv2.getRotationMatrix2D(center, 45, 1.0)

# .wrapAffine() = 1. input 2. angle, area (width, height)
img_rotate = cv2.warpAffine(img, angle, (width, height))

cv2.imshow('Rotated', img_rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()