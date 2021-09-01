import numpy as np, cv2

def filter(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)
    ycenter, xcenter = mask.shape[0]//2, mask.shape[1]//2

    for i in range(ycenter, rows - ycenter):
        for j in range(xcenter, cols - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1
            x1, x2 = j - xcenter, j + xcenter + 1
            roi = image[y1:y2, x1:x2].astype('float32')
            tmp = cv2.multiply(roi, mask)
            dst[i, j] = cv2.sumElems(tmp)[0]
    return dst

image = cv2.imread("efltop.jfif", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류")

blue, green, red = cv2.split(image)
zero = np.zeros(image.shape[:2], np.uint8)

data1 = [1/9, 1/9, 1/9,
        1/9, 1/9, 1/9,
        1/9, 1/9, 1/9]
mask1 = np.array(data1, np.float32).reshape(3, 3)

data2 = [0, -1, 0,
         -1, 5, -1,
         0, -1, 0]
mask2 = np.array(data2, np.float32).reshape(3, 3)

blur1 = filter(blue, mask1)
blur1 = blur1.astype('uint8')
blur2 = filter(green, mask1)
blur2 = blur2.astype('uint8')
blur3 = filter(red, mask1)
blur3 = blur3.astype('uint8')
list_blur = [blur1, blur2, blur3]

blur = cv2.merge(list_blur)

sharpen1 = filter(blue, mask2)
sharpen1 = cv2.convertScaleAbs(sharpen1)
sharpen2 = filter(green, mask2)
sharpen2 = cv2.convertScaleAbs(sharpen2)
sharpen3 = filter(red, mask2)
sharpen3 = cv2.convertScaleAbs(sharpen3)
list_sharpen = [sharpen1, sharpen2, sharpen3]

sharpen = cv2.merge(list_sharpen)

filter2d = cv2.filter2D(image, -1, mask1)
cv2.imshow("filter2d", filter2d)

cv2.imshow("image", image)
cv2.imshow("blur", blur)
cv2.imshow("sharpen", sharpen)

cv2.waitKey(0)