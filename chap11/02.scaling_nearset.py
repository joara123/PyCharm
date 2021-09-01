import numpy as np, cv2
from Common.utils import scaling #이놈은 arrange할 때 img.shape[] 이케해서

def scaling_nearset(img, size):
    dst = np.zeros(size[::-1], img.dtype)
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    i = np.arange(0, size[1], 1) #이놈은 size루다가
    j = np.arange(0, size[0], 1)
    i, j = np.meshgrid(i, j)
    y, x = np.int32(i / ratioY), np.int32(j / ratioX)
    dst[i, j] = img[y, x]

    return dst

image = cv2.imread("efltop.jfif", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

dst1 = scaling(image, (350, 400))
dst2 = scaling_nearset(image, (350, 400))

cv2.imshow("image", image)
cv2.imshow("dst1- forward mapping", dst1)
cv2.imshow("dst2- NN interpolation", dst2)
cv2.waitKey(0)