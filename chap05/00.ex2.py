import numpy as np, cv2

image = cv2.imread("efltop.jfif", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류 발생")


mask1 = cv2.add(image[0:500, 20:300], 100)
mask2 = cv2.add(image[0:100, 150:250], 150)

cv2.imshow('mask1', mask1)
#cv2.imshow('mask2', mask2)
cv2.waitKey(0)