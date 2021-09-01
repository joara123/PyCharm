import numpy as np, cv2

def draw_histo(hist, shape=(200, 256)):
    hist_img = np.full( shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)
    gap = hist_img.shape[1]/hist.shape[0]             # 한 계급 너비

    for i, h in enumerate(hist):
        x = int(round(i * gap))                         # 막대 사각형 시작 x 좌표
        w = int(round(gap))
        roi = (x, 0, w, int(h))
        cv2.rectangle(hist_img, roi, 0, cv2.FILLED)

    return cv2.flip(hist_img, 0)                        # 영상 상하 뒤집기 후 반환

image = cv2.imread("efltop.jfif", cv2.IMREAD_GRAYSCALE) # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류")

bins, ranges = [256], [0, 256]

# 히스토그램 계산
hist = cv2.calcHist([image], [0], None, bins, ranges)

#################################################
# 히스토그램 누적합 계산
# 이곳에 코드를 작성하세요.
# 주의사항 1. 교과서 참조하지 않고 구현할것!
# 주의사항 2. list comprehension 사용하지 말것

arr = np.zeros((1, 256), np.float32) #누적빈도수
arr[0][0] = hist[0]

for i in range(1, 256):
    arr[0][i] = hist[i] + arr[0][i-1]

for j in range(256): #정규화누적합
    arr[0][j] = arr[0][j] / arr[0][255]

for k in range(256): #누적합*최댓값
    arr[0][k] = arr[0][k] * 255

#arr1 = np.array(arr, np.uint32)

#print(arr1)

# 히스토그램 평활화 이미지를 아래에 저장하시오.
#dst1 = [[arr1[val] for val in row] for row in image]

#dst_student_image = image

for i in image:
    for j in i:
        dst_student_image = arr[0][j]
dst_student_image = np.array(dst_student_image, np.uint8)


#################################################


hist_student = cv2.calcHist([dst_student_image], [0], None, bins, ranges)   # 히스토그램 계산

# 학생이 구현한 히스토그램 출력
hist_img = draw_histo(hist)
hist_eq_img_student = draw_histo(hist_student)
cv2.imshow("image", image)
cv2.imshow("hist_img", hist_img)
cv2.imshow("dst_student_image", dst_student_image)
cv2.imshow("Student_hist", hist_eq_img_student)

cv2.waitKey(0)
