import cv2

video = cv2.VideoCapture("videos/Person_Typing_Fast.mp4")

while (video.isOpened()):
    ret, frame = video.read()

    frameResize = frame
    frameResize = cv2.resize(frameResize, (1920, 1080))

    alto = str(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    ancho = str(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    resolucion = "Resolucion: " + str(ancho + "x" + alto)
    fps = "FPS: " + str(round(video.get(cv2.CAP_PROP_FPS)))
    bitrate = "Bitrate: " + str(
        round(video.get(cv2.CAP_PROP_BITRATE))) + " kbps."

    cv2.putText(frameResize, fps, (7, 40), cv2.FONT_HERSHEY_SIMPLEX, .5,
                (100, 255, 0), 1, cv2.LINE_AA)
    cv2.putText(frameResize, resolucion, (7, 55), cv2.FONT_HERSHEY_SIMPLEX, .5,
                (100, 255, 0), 1, cv2.LINE_AA)
    cv2.putText(frameResize, bitrate, (7, 70), cv2.FONT_HERSHEY_SIMPLEX, .5,
                (100, 255, 0), 1, cv2.LINE_AA)

    if ret:
        cv2.imshow("Video", frameResize)
        if cv2.waitKey(30) == ord("s"):
            break
    else:
        break

video.release()
cv2.destroyAllWindows
