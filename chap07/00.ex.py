import numpy as np, cv2
from Common.utils import draw_histo

image = cv2.imread("efltop.jfif", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

(x, y), (w, h) = (180, 37), (100, 100)
roi_img = image[y:y+h, x:x+w]

arr = np.zeros((1, 255), np.uint32) #빈도수
for row in roi_img:
    for pixel in row:
        for i in range(255):
            if (i == pixel):
                arr[0][i] += 1

print(arr)
arr2 = np.zeros((1, 255), np.uint32) #누적 빈도수
arr2[0][0] = arr[0][0]
arr2[0][1] = arr[0][0] + arr[0][1]

for i in range(2, 255): #누적 빈도수 넣음
    arr2[0][i] = arr2[0][i-1] + arr[0][i]

for j in range(255): #정규화누적합
    arr2[0][i] = arr2[0][i] / 10000

for k in range(255): #누적합*최댓값
    arr2[0][i] = arr2[0][i] * 255

