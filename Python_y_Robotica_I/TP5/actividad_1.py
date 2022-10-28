import cv2

img = cv2.imread('imagenes/vehiculo.jpg')

imgOut = img[140:160, 110:175]

cv2.imshow('Patente', imgOut)
cv2.imwrite("imagenes/patente.png", imgOut)
cv2.waitKey(5000)

cv2.destroyAllWindows()
