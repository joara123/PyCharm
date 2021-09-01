import numpy as np, cv2
from Common.utils import draw_histo

image = cv2.imread("cannay_tset.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

(x, y), (w, h) = (180, 37), (100, 100)
roi_img = image[y:y+h, x:x+w]

arr = np.zeros((1, 255))

for row in roi_img:
    for pixel in row:
        for i in range(255):
            if (i == pixel):
                arr[0][i] += 1

low = 0
for i in arr[0]:
    if(i > 0):
        break
    low = low + 1

high1 = 0
for i in reversed(arr[0]):
    if(i > 0):
        break
    high1 = high1 + 1
high = 255 - high1


hist = cv2.calcHist([roi_img], [0], None, [32], [0, 256])
hist_img = draw_histo(hist)

cv2.imshow("hist_img", hist_img)
#cv2.imshow("hist_dst_img", hist_dst_img)

cv2.waitKey(0)