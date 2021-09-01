import numpy as np, cv2

image = cv2.imread("efltop.jfif", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

data = [1/9, 1/9, 1/9,
        1/9, 1/9, 1/9,
        1/9, 1/9, 1/9]
mask = np.array(data, np.float32).reshape(3, 3)

rows, cols = image.shape[:2]
dst = np.zeros((rows, cols), np.float32)
ycenter, xcenter = mask.shape[0]//2, mask.shape[1]//2






sum = 0
for i in range(ycenter, rows - ycenter):
    for j in range(xcenter, cols - xcenter):
        for u in range(mask.shape[0]):
            for v in range(mask.shape[1]):
                y, x = i + u - ycenter, j + v - xcenter
                sum += image[y, x] * mask[u, v]
        dst[i, j] = sum


