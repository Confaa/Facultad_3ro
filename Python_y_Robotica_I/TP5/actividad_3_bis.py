import cv2
import numpy as np

img = cv2.imread("imagenes/ruta.jpg")

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lowYellow = (10, 100, 20)
highYellow = (21, 255, 255)

maskYellow = cv2.inRange(imgHSV, lowYellow, highYellow)
maskYellowBis = cv2.bitwise_and(img, img, mask=maskYellow)

imgGris = cv2.cvtColor(maskYellowBis, cv2.COLOR_BGR2GRAY)

borders = cv2.Canny(imgGris, 100, 500)
borders = cv2.dilate(borders, None, iterations=1)
borders = cv2.erode(borders, None, iterations=1)

contours, hierarchy = cv2.findContours(borders, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (60, 190, 50), 2)

texto = "Alerta al conductor"

cv2.putText(img, texto, (50, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (60, 190, 50),
            2)

cv2.imshow("Imagen", img)

cv2.waitKey(5000)
cv2.destroyAllWindows()
