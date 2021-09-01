import numpy as np, cv2

def translate(img, pt):
    dst = np.zeros(img.shape, img.dtype)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            x, y = np.add((j, i), pt)
            if(0 <= y < img.shape[0] and 0 <= x < img.shape[1]):
                dst[i, j] = img[y, x]

    return dst

image = cv2.imread("efltop.jfif", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

M = np.float32([[1, 0, 50], [0, 1, 60]])
trans = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

dst1 = translate(image, (50, 60))

cv2.imshow("image", image)
cv2.imshow("openCV trans", trans)
cv2.imshow("dst1", dst1)
cv2.waitKey(0)