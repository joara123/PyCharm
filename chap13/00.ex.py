import matplotlib.pylab as pylab
import numpy as np, cv2
import numpy.fft as fp
from Common.utils import fftshift, dft2, idft2, calc_spectrum, FFT, IFFT, fft2

image = cv2.imread("lion.png", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

img = np.copy(image)

for n in range(img.shape[1]):
    img[:, n] = np.cos(np.pi*1/8*n)*2

pylab.imshow(img)

dft = fft2(image)
spe1 = calc_spectrum(dft)

sy, sx = np.divmod(image.shape, 2)[0]
spe1[sy-3:sy+3, 0:sx-7] = 0
spe1[sy-3:sy+3, sx+7:sx*2] = 0 #0인 직선 두개 찍찍


cv2.imshow("spe1", spe1)
#cv2.imshow("spe2", spe2)
cv2.imshow("img", img)
cv2.imshow("image", image)
cv2.waitKey(0)