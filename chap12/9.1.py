import matplotlib.pylab as pylab
import numpy as np
import numpy.fft as fp

im = np.zeros([32, 32])
im1 = np.copy(im)

magnitude = 1 #진폭
phase = 0 #위상
wavelength = 32 #파장
freauency = 1/wavelength #진동수
omega = 2 * np.pi * freauency #각 주파수(각 속도)

for n in range(im.shape[1]):
    im1[:, n] += np.cos(omega*n + phase)

pylab.figure(figsize=(10, 7))
pylab.imshow(im1, cmap='gray')
pylab.show()