import numpy as np, cv2

BGR_img = cv2.imread("efltop.jfif", cv2.IMREAD_COLOR)
if BGR_img is None: raise Exception("영상파일 읽기 오류")

white = np.array([255, 255, 255], np.uint8)
zero = np.zeros(BGR_img.shape[:2], np.uint8)
CMY_img = white - BGR_img
CMY = cv2.split(CMY_img)

black = cv2.min(CMY[0], cv2.min(CMY[1], CMY[2]))
Yellow, Magenta, Cyan = CMY - black

blue_img = cv2.merge([Yellow, zero, zero])
green_img = cv2.merge([zero, Magenta, zero])
red_img = cv2.merge([zero, zero, Cyan])

cv2.imshow("blue_img", blue_img)
cv2.imshow("green_img", green_img)
cv2.imshow("red_img", red_img)
cv2.waitKey(0)