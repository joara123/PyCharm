import numpy as np, math
import cv2, time
import matplotlib.pyplot as plt

def print_matInfo(name, image):
    if image.dtype == 'uint8':  mat_type = 'CV_8U'
    elif image.dtype == 'int8': mat_type = 'CV_8S'
    elif image.dtype == 'uint16': mat_type = 'CV_16U'
    elif image.dtype == 'int16': mat_type = 'CV_16S'
    elif image.dtype == 'float32': mat_type = 'CV_32F'
    elif image.dtype == 'float64': mat_type = 'CV_64F'
    nchanel = 3 if image.ndim == 3 else 1

    print("%12s: depth(%s), channels(%s) -> mat_type(%sC%d)"
          % (name, image.dtype, nchanel, mat_type, nchanel))

def put_string(frame, text, pt, value, color = (120, 200, 90)):
    text += str(value)
    shade = (pt[0] + 2, pt[1] + 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, shade, font, 0.7, (0, 0, 0), 2)
    cv2.putText(frame, text, pt, font, 0.7, color, 2)

def draw_histo(hist, shape=(200, 256)):
    hist_img = np.full(shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)
    gap = hist_img.shape[1]/hist.shape[0]

    for i, h in enumerate(hist):
        x = int(round(i * gap))
        w = int(round(gap))
        cv2.rectangle(hist_img, (x, 0, w, int(h)), 0, cv2.FILLED)

    return cv2.flip(hist_img, 0)

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

def contain(p, shape):
    return 0<= p[0] < shape[0] and 0<= p[1] < shape[1]

def affine_transform(img, mat, size):
    rows, cols = img.shape[:2]
    inv_mat = cv2.invertAffineTransform(mat)
    #size = img.shape[::-1]

    pts = [np.dot(inv_mat, (j, i, 1)) for i in range(rows) for j in range(cols)]
    dst = [bilinear_value(img, p) if contain(p, size) else 0 for p in pts]
    dst = np.reshape(dst, (rows, cols)).astype('uint8')

def scaling(img, size):
    dst = np.zeros(size[::-1], img.dtype)
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    y = np.arange(0, img.shape[0], 1)
    x = np.arange(0, img.shape[1], 1)
    y, x = np.meshgrid(y, x)
    i, j = np.int32(y * ratioY), np.int32(x * ratioX)
    dst[i, j] = img[y, x]
    return dst

def scaling2(img, size):
    dst = np.zeros(size[::-1], img.dtype)
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            i, j = int(y * ratioY), int(x * ratioX)
            dst[i, j] = img[y, x]
    return dst

def scaling_nearset(img, size):
    dst = np.zeros(size[::-1], img.dtype)
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    i = np.arange(0, size[1], 1) #이놈은 size루다가
    j = np.arange(0, size[0], 1)
    i, j = np.meshgrid(i, j)
    y, x = np.int32(i / ratioY), np.int32(j / ratioX)
    dst[i, j] = img[y, x]

    return dst

def exp(knN):
    th = -2 * math.pi * knN
    return complex(math.cos(th), math.sin(th))

def dft(g):
    N = len(g)
    dst = [sum(g[n] * exp(k*n/N) for n in range(N)) for k in range(N)]
    return np.array(dst)

def idft(g):
    N = len(g)
    dst = [sum(g[n] * exp(+k*n/N) for n in range(N)) for k in range(N)]
    return np.array(dst) / N

def calc_spectrum(complex):
    if complex.ndim == 2:
        dst = abs(complex)
    else:
        dst = cv2.magnitude(complex[:,:,0], complex[:,:,1])
    dst = cv2.log(dst + 1)
    cv2.normalize(dst, dst, 0, 255, cv2.NORM_MINMAX)
    return cv2.convertScaleAbs(dst)

def fftshift(img):
    dst = np.zeros(img.shape, img.dtype)
    h, w = dst.shape[:2]
    cy, cx = h // 2, w // 2
    dst[h-cy:, w-cx:] = np.copy(img[0:cy, 0:cx])
    dst[0:cy, 0:cx] = np.copy(img[h-cy:, w-cx:])
    dst[0:cy, w - cx:] = np.copy(img[h-cy:, 0:cx])
    dst[h - cy:, 0:cx] = np.copy(img[0:cy, w-cx:])

def dft2(image):
    tmp = [dft(row) for row in image]
    dst = [dft(row) for row in np.transpose(tmp)]
    return np.transpose(dst)

def idft2(image):
    tmp = [idft(row) for row in image]
    dst = [idft(row) for row in np.transpose(tmp)]
    return np.transpose(dst)

def ck_time(mode=0):
    global stime
    if(mode == 0):
        stime = time.perf_counter()
    elif(mode == 1):
        etime = time.perf_counter()
        print("수행시간 = %.5f sec" % (etime - stime))

def zeropadding(img):
    h, w = img.shape[:2]
    m = 1 << int(np.ceil(np.log2(h)))
    n = 1 << int(np.ceil(np.log2(w)))
    dst = np.zeros((m, n), img.dtype)
    dst[0:h, 0:w] = img[:]
    return dst

def butterfly(pair, L, N, dir):
    for k in range(L):
        Geven, Godd = pair[k], pair[k + L]
        pair[k] = Geven + Godd * exp(dir * k / N)
        pair[k + L] = Geven - Godd * exp(dir * k / N)

def parring(g, N, dir, start=0, stride=1):
    if N == 1:  return [g[start]]
    L = N // 2
    sd = stride * 2
    part1 = parring(g, L, dir, start, sd)
    part2 = parring(g, L, dir, start + stride, sd)
    pair = part1 + part2
    butterfly(pair, L, N, dir)
    return pair

def fft(g):
    return parring(g, len(g), 1)

def ifft(g):
    fft = parring(g, len(g), -1)
    return [v / len(g) for v in fft]

def fft2(image):
    pad_img = zeropadding(image)
    tmp = [fft(row) for row in pad_img]
    dst = [fft(row) for row in np.transpose(tmp)]
    return np.transpose(dst)

def ifft2(image):
    tmp = [ifft(row) for row in image]
    dst = [ifft(row) for row in np.transpose(tmp)]
    return np.transpose(dst)

def FFT(image, mode=2):
    if mode == 1:   dft = fft2(image)
    elif mode == 2: dft = np.fft.fft2(image)
    elif mode == 3: dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft = fftshift(dft)
    spectrum = calc_spectrum(dft)
    return dft, spectrum

def IFFT(dft, shape, mode=2):
    dft = fftshift(dft)
    if mode == 1:   img = ifft2(dft).real
    if mode == 2:   img = np.fft.ifft2(dft).real
    if mode == 3:   img = cv2.idft(dft, flags=cv2.DFT_SCALE)[:,:,0]
    img = img[:shape[0], :shape[1]]
    return cv2.convertScaleAbs(img)