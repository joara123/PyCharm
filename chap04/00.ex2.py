import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    global title, pt, size
    size = 1
    size2 = 1

    if event == cv2.EVENT_LBUTTONDOWN:
        if pt[0] < 0: pt = (x, y)
        else:
            roi = (x, y, 30, 30)
            cv2.rectangle(image, roi, (255, 0, 0), size)
            cv2.imshow(title, image)
            pt = (-1, -1)

    elif event == cv2.EVENT_RBUTTONDOWN:
        if pt[0] < 0: pt = (x, y)
        else:

            cv2.circle(image, pt, size2, (0, 0, 255), size)
            cv2.imshow(title, image)
            pt = (-1, -1)

    def pix_bar(value):
        global image, title

        size = value + 1
        cv2.imshow(title, image)

    def rad_bar(value):
        global image, title

        size2 = value + 1
        cv2.imshow(title, image)

    cv2.createTrackbar('pixel', title, size, 10, pix_bar)
    cv2.createTrackbar('radius', title, size2, 50, rad_bar)

image = np.full((300, 500, 3), (255, 255, 255), np.uint8)

pt = (-1, -1)
title = "Draw Event"

cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)