import numpy as np, cv2, time
from Common.utils import dft, idft, calc_spectrum, fftshift

def dft2(image):
    tmp = [dft(row) for row in image]
    dst = [dft(row) for row in np.transpose(tmp)]
    return np.transpose(dst)

def idft2(image):
    tmp = [idft(row) for row in image]
    dst = [idft(row) for row in np.transpose(tmp)]
    return np.transpose(dst)

image = cv2.imread("lion.png", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

spectrum1 = np.fft.fft2(image)
#spectrum1 = calc_spectrum(dft)

spectrum2 = np.fft.fftshift(spectrum1)
sy, sx = np.divmod(spectrum2.shape, 2)[0]
spectrum2[sy-10:sy+10, sx-10:sx+10] = 0

spectrum3 = np.fft.ifftshift(spectrum2)

idft = np.fft.ifft2(spectrum3).real

cv2.imshow("image", image)
#cv2.imshow("spectrum1", spectrum1)
#cv2.imshow("specturm2", spectrum2)
#cv2.imshow("specturm3", spectrum3)
cv2.imshow("idft_img", cv2.convertScaleAbs(idft))

cv2.waitKey(0)