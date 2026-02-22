import cv2
import numpy as np

img = np.zeros((400, 600, 3), dtype=np.uint8)

# Drawing line vertical
for x in range(0, 600, 100):
    cv2.line(img, (x, 0), (x, 400), (50, 50, 50), 1)

# Drawing line horizontal
for y in range(0, 400, 100):
    cv2.line(img, (0, y), (600, y), (50, 50, 50), 1)

cv2.imshow('Board', img)
cv2.waitKey(0)
cv2.destroyAllWindows()