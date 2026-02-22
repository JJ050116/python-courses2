import cv2
import numpy as np

img = np.zeros((400, 600, 3), dtype=np.uint8)

for x in range(0, 600, 100):
    cv2.line(img, (x, 0), (x, 400), (50, 50, 50), 1)

for y in range(0, 600, 100):
    cv2.line(img, (0, y), (400, y), (50, 50, 50), 1)

x1, y1 = 200, 100
x2, y2 = 400, 300

cv2.rectangle(img, (x1, y1), (x2, y2), (22, 49, 224), 3)

cv2.putText(img, "My Area", (210, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (7, 227, 69), 2)

roi_img = img[y1:y2, x1:x2]

cv2.imshow('Main image with grid', img)
cv2.imshow('Cropped ROI', roi_img)

cv2.waitKey(0)
cv2.destroyAllWindows()