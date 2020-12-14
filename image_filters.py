import cv2 as cv
from cv2 import data as cascades
import numpy as np
import os


def equalize_histogram(src_img):
    img_yuv = cv.cvtColor(src_img, cv.COLOR_BGR2YUV)
    img_yuv[:, :, 0] = cv.equalizeHist(img_yuv[:, :, 0])
    dst_img = cv.cvtColor(img_yuv, cv.COLOR_YUV2BGR)
    return dst_img


def fill_holes(mask):
    mask_flood_fill = mask.copy()
    h, w = mask_flood_fill.shape[:2]
    mask_temp = np.zeros((h+2, w+2), np.uint8)
    cv.floodFill(mask_flood_fill, mask_temp, (0, 0), 255)
    mask2 = cv.bitwise_not(mask_flood_fill)
    return mask2 | mask


def red_eye_reduction(src_img):
    img_out = src_img.copy()
    eyes_cascade = cv.CascadeClassifier(os.path.join(cascades.haarcascades, "haarcascade_eye.xml"))
    eyes = eyes_cascade.detectMultiScale(src_img, scaleFactor=1.3, minNeighbors=4, minSize=(100, 100))
    for (x, y, w, h) in eyes:
        eye = src_img[y:y + h, x:x + w]
        b = eye[:, :, 0]
        g = eye[:, :, 1]
        r = eye[:, :, 2]

        bg = cv.add(b, g)
        mask = (r > 150) & (r > bg)
        mask = mask.astype(np.uint8) * 255
        mask = fill_holes(mask)
        mask = cv.dilate(mask, None, anchor=(-1, -1), iterations=3, borderType=1, borderValue=1)

        mean = bg / 2
        mask = mask.astype(np.bool)[:, :, np.newaxis]
        mean = mean[:, :, np.newaxis]

        eye_out = eye.copy()
        np.copyto(eye_out, mean, where=mask, casting='unsafe')
        img_out[y:y + h, x:x + w, :] = eye_out
    return img_out


def main():
    fuck = os.path.join("app", "static", "mock", "lena.png")
    src_img = cv.imread(fuck)
    out_img = red_eye_reduction(src_img)
    out_img = equalize_histogram(out_img)
    cv.imshow("SOURCE", src_img)
    cv.imshow("FILTERED", out_img)
    cv.waitKey(0)


if __name__ == "__main__":
    main()
