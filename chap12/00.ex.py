import matplotlib.pylab as pylab
import numpy as np, math, cv2
from Common.utils import dft2, dft, calc_spectrum, fftshift, idft2, idft, scaling

im = np.zeros([32, 32])

im1 = np.copy(im)
magnitude1 = 0.3 #진폭
phase1 = 0 #위상
omega1 = 1 #각 주파수(각 속도)
for n in range(im.shape[1]):
    im1[:, n] += np.cos(omega1*n + phase1)

im2 = np.copy(im)
magnitude2 = 0.5 #진폭
phase2 = 0 #위상
omega2 = 4 #각 주파수(각 속도)
for n in range(im.shape[1]):
    im2[:, n] += np.cos(omega2*n + phase2)

im3 = np.copy(im)
magnitude3 = -0.2 #진폭
phase3 = 10 #위상
omega3 = 16 #각 주파수(각 속도)
for n in range(im.shape[1]):
    im3[:, n] += np.cos(omega3*n + phase3)

im4 = np.copy(im)
magnitude4 = -0.8 #진폭
phase4 = 20 #위상
omega4 = 5 #각 주파수(각 속도)
for n in range(im.shape[1]):
    im4[:, n] += np.cos(omega4*n + phase4)

g = im1 + im2 + im3 + im4
dft = dft2(g) #2d dft
spe = calc_spectrum(dft)
spe2 = np.fft.fftshift(spe)
idft = idft2(dft).real #2d idft

dst1 = scaling(spe2, (150, 200)) #확대

pylab.figure(figsize=(10, 7))
pylab.imshow(g, cmap='gray')
pylab.show()


cv2.imshow("spe", spe)
cv2.imshow("spe2", spe2)
cv2.imshow("idft", cv2.convertScaleAbs(idft))
cv2.imshow("dst1", dst1)
cv2.waitKey(0)