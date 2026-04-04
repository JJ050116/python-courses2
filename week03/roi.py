import cv2
# Library Numpy using for handle array or list in python or calculate multi dimension (more than 1D)
# Numpy it's was so good at high calculation about Com Sci 
import numpy as np

# paper
# np.zeros() = 1. size of paper (height<px>, widht<px>) 2. primary color (RGB)
img = np.zeros((400, 600, 3))

# Horizontal
for x in range(0, 600, 100):
    # .line() = 1. paper 2. point1 3. point2 4. color(BGR) 5. line bold
    cv2.line(img, (x, 0), (x, 400), (179, 173, 173), 1)

# Vertical
for y in range(0, 400, 100):
    cv2.line(img, (0, y), (600, y), (179, 173, 173), 1)

# Drawing a square (center) table
x1, y1 = 200, 100
x2, y2 = 400, 300

# Drawing a rectangle
# .rectangle() = 1. img (paper) 2. ROI do you want to drawing
cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)


# Text
# .putText() = 1. img (paper) 2. message (string) 3. ROI 4. font 5. font_size 6. color 7. bold
cv2.putText(img, 'My ROI Area', (210, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

# Cropped ROI
roi_img = img[y1:y2, x1:x2]

# show result
cv2.imshow('Main Image with Grid', img)
cv2.imshow('Cropped ROI', roi_img)

cv2.waitKey(0)
cv2.destroyAllWindows()