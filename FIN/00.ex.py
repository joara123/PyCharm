import numpy as np, cv2

xml = "haarcascade_frontalface_alt2.xml"
face_cascade = cv2.CascadeClassifier(xml)

image = cv2.imread("per1.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 에러")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.05, 5)

if faces.any():
    for (x, y, w, h) in faces:
        face_img = image[y:y+h, x:x+w]
        face_img = cv2.resize(face_img, dsize=(0,0), fx = 0.04, fy = 0.04)
        face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA)
        image[y:y+h, x:x+w] = face_img

cv2.imshow("image", image)
cv2.waitKey(0)