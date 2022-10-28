import cv2
import numpy as np

img = cv2.imread("imagenes/semaforo2.jpg")

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lowRed1 = np.array([0, 100, 20], np.uint8)
highRed1 = np.array([8, 255, 255], np.uint8)
lowRed2 = np.array([175, 100, 20], np.uint8)
highRed2 = np.array([179, 255, 255], np.uint8)

maskRed1 = cv2.inRange(imgHSV, lowRed1, highRed1)
maskRed2 = cv2.inRange(imgHSV, lowRed1, highRed2)

maskRed = cv2.add(maskRed1, maskRed2)

maskRedVis = cv2.bitwise_and(img, img, mask=maskRed)

cv2.imshow('original', img)
cv2.imshow('maskRed', maskRed)
cv2.imshow('maskRedVis', maskRedVis)

cv2.waitKey(5000)
cv2.destroyAllWindows()