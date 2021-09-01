import numpy as np, cv2

def scaling_nearset(img, size):
    dst = np.zeros(size[::-1], img.dtype)
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    i = np.arange(0, size[1], 1) #이놈은 size루다가
    j = np.arange(0, size[0], 1)
    i, j = np.meshgrid(i, j)
    y, x = np.int32(i / ratioY), np.int32(j / ratioX)
    dst[i, j] = img[y, x]

    return dst

def preprocessing():
    image = cv2.imread("per1.jpg", cv2.IMREAD_COLOR)
    if image is None: return None, None
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    return image, gray

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
image, gray = preprocessing()
if image is None: raise Exception("영상파일 읽기 에러")

faces = face_cascade.detectMultiScale(gray, 1.1, 2, 0, (100, 100))
if faces.any():
    for(x, y, w, h) in faces:
        # 얼굴 영역 구하기
        face_image = image[y:y + h, x:x + w]
        cv2.rectangle(image, faces[0], (0, 0, 0))

        # 구한 얼굴영역 R, G, B로 나누기
        # R, G, B 각각 따로 사이즈 작게 했다가 크게하기 << 모자이크 방법
        list_bgr = cv2.split(face_image)
        dst1 = scaling_nearset(list_bgr[0], (10, 10))
        dst1 = scaling_nearset(dst1, (w, h))  # B

        dst2 = scaling_nearset(list_bgr[1], (10, 10))
        dst2 = scaling_nearset(dst2, (w, h))  # G

        dst3 = scaling_nearset(list_bgr[2], (10, 10))
        dst3 = scaling_nearset(dst3, (w, h))  # R

        # 나눈 R, G, B 합치기
        dst_list = [dst1, dst2, dst3]
        dst = cv2.merge(dst_list)

        # 합친 얼굴영역 다시 이미지에다가 삽입
        image[y:y + h, x:x + w] = dst

    cv2.imshow("mosaic", image)

else:
    print("얼굴 미검출")

cv2.waitKey(0)