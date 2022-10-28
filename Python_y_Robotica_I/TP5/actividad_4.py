import cv2

video = cv2.VideoCapture(0)

while video.isOpened():
    ret, frame= video.read()
    cv2.imshow("En vivo",frame)
    if cv2.waitKey(1) == ord('s'):
        break

video.release()
cv2.destroyAllWindows()