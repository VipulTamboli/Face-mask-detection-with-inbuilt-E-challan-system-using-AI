import cv2
import numpy as pd 
img = cv2.imread('image1.png')
height , width = img.shape[:2]

start_row, start_col = int(height*.10), int(width *.02)

end_row , end_col =  int(height*.45), int(width *.30)

cropped = img[start_row:end_row, start_col: end_col]

cv2.imshow('Original', img)

# cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Cropped', cropped)

cv2.imwrite("image2.png", cropped) 
cv2.waitKey(0)

cv2.destroyAllWindows()