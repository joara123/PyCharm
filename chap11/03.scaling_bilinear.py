import numpy as np, cv2
from Common.utils import scaling_nearset

def bilinear_value(img, pt):
    x, y = np.int32(pt)
    if x >= img.shape[1]-1: x = x-1
    if y >= img.shape[0]-1: y = y-1

    p1, p2, p3, p4 = np.float32(img[y:y+2, x:x+2].flatten())

    alpha, beta = pt[1] - y, pt[0] - x
    M1 = p1 + alpha * (p3 - p1)
    M2 = p2 +alpha * (p4 - p2)
    P = M1 + beta * (M2 - M1)
    return np.clip(P, 0, 255)

def scaling_bilinear(img, size):
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])

    dst = [[bilinear_value(img, (j/ratioY, i/ratioX))
            for j in range(size[0])]
           for i in range(size[1])]

    return np.array(dst, img.dtype)

