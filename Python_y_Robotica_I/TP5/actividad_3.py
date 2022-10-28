import cv2
import numpy as np

img = cv2.imread("imagenes/cubo.jpg")

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lowBlue = np.array([95, 50, 50])

# Realice cambios en el rango bajo del azul, colocando el componente H en 95,
# sino no lo detectaba correctamente

highBlue = np.array([130, 255, 255])

maskBlue = cv2.inRange(imgHSV, lowBlue, highBlue)

maskBlueVis = cv2.bitwise_and(img, img, mask=maskBlue)

cv2.imshow('original', img)
cv2.imshow('maskRed', maskBlue)
cv2.imshow('maskRedVis', maskBlueVis)

cv2.waitKey(5000)
cv2.destroyAllWindows()
