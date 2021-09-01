import numpy as np, cv2
from Common.utils import scaling2, scaling

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
    x, y, w, h = faces[0]

    face_image = image[y:y+h, x:x+w]
    cv2.rectangle(image, faces[0], (255, 0, 0), 1)

    dst1 = cv2.resize(face_image, (0, 0), fx=0.04, fy=0.04)
    dst2 = cv2.resize(dst1, (w, h), interpolation=cv2.INTER_NEAREST)
    image[y:y + h, x:x + w] = dst2
    cv2.imshow("imageR", image)
else:
    print("얼굴 미검출")


cv2.waitKey(0)