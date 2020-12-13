import cv2 as cv
from cv2 import data as cascades
import numpy as np
import os


def equalize_histogram(src_img):
    img_yuv = cv.cvtColor(src_img, cv.COLOR_BGR2YUV)
    img_yuv[:, :, 0] = cv.equalizeHist(img_yuv[:, :, 0])
    dst_img = cv.cvtColor(img_yuv, cv.COLOR_YUV2BGR)
    return dst_img


def fillHoles(mask):
    maskFloodfill = mask.copy()
    h, w = maskFloodfill.shape[:2]
    maskTemp = np.zeros((h+2, w+2), np.uint8)
    cv.floodFill(maskFloodfill, maskTemp, (0, 0), 255)
    mask2 = cv.bitwise_not(maskFloodfill)
    return mask2 | mask



def red_eye_reduction(src_img):
    # Read image
    img = src_img

    # Output image
    imgOut = img.copy()

    # Load HAAR cascade
    eyesCascade = cv.CascadeClassifier(os.path.join(cascades.haarcascades, "haarcascade_eye.xml"))

    # Detect eyes
    eyes = eyesCascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(100, 100))
    for (x, y, w, h) in eyes:
        # Extract eye from the image.
        eye = img[y:y + h, x:x + w]
        # Split eye image into 3 channels
        b = eye[:, :, 0]
        g = eye[:, :, 1]
        r = eye[:, :, 2]

        # Add the green and blue channels.
        bg = cv.add(b, g)

        # Simple red eye detector
        mask = (r > 150) & (r > bg)

        # Convert the mask to uint8 format.
        mask = mask.astype(np.uint8) * 255

        # Clean up mask by filling holes and dilating
        mask = fillHoles(mask)
        mask = cv.dilate(mask, None, anchor=(-1, -1), iterations=3, borderType=1, borderValue=1)

        # Calculate the mean channel by averaging
        # the green and blue channels. Recall, bg = cv2.add(b, g)
        mean = bg / 2
        mask = mask.astype(np.bool)[:, :, np.newaxis]
        mean = mean[:, :, np.newaxis]

        # Copy the eye from the original image.
        eyeOut = eye.copy()
        # Copy the mean image to the output image.
        np.copyto(eyeOut, mean, where=mask, casting='unsafe')
        # Copy the fixed eye to the output image.
        imgOut[y:y + h, x:x + w, :] = eyeOut

    return imgOut

def main():
    import os
    src_path = os.path.join("app", "static", "mock", "child.jpg")
    src_img = cv.imread(src_path)
    out_img = red_eye_reduction(src_img)
    cv.imshow("SOURCE", src_img)
    cv.imshow("FILTERED", out_img)
    cv.waitKey(0)


if __name__ == "__main__":
    main()
