import numpy as np, cv2

def onThreshold(th):
    th[0] = cv2.getTrackbarPos("Hue_th1", "result")
    th[1] = cv2.getTrackbarPos("Hue_th1", "result")

    _, result = cv2.threshold(hue, th[1], 255, cv2.THRESH_TOZERO_INV)
    