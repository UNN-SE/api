import cv2 as cv


def equalize_histogram(src_img):
    img_yuv = cv.cvtColor(src_img, cv.COLOR_BGR2YUV)
    img_yuv[:, :, 0] = cv.equalizeHist(img_yuv[:, :, 0])
    dst_img = cv.cvtColor(img_yuv, cv.COLOR_YUV2BGR)
    return dst_img


def main():
    import os
    src_path = os.path.join("app", "static", "mock", "lena.png")
    src_img = cv.imread(src_path)
    out_img = equalize_histogram(src_img)
    cv.imshow("SOURCE", src_img)
    cv.imshow("FILTERED", out_img)
    cv.waitKey(0)


if __name__ == "__main__":
    main()
