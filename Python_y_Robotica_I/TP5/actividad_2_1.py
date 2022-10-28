import cv2

img = cv2.imread("imagenes/monedas2.jpg")

imgGris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

borders = cv2.Canny(imgGris, 100, 500)

borders = cv2.dilate(borders, None, iterations=1)
borders = cv2.erode(borders, None, iterations=1)

contours, hierarchy = cv2.findContours(borders, cv2.RETR_EXTERNAL,
                                        cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

text = "Contornos encontrados: " + str(len(contours))

cv2.putText(img, text, (15, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0),
            1)
# Modifique el quinto parametro para que entre el texto en la imagen
cv2.imshow("Image", img)

cv2.waitKey(5000)
cv2.destroyAllWindows()
