import cv2

print(cv2.__version__)

width = 640
height = 360

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
# cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
while True:
    _, frame = cam.read()
    if _:
        cv2.imshow("My Webcam", frame)
        cv2.moveWindow("My Webcam", 0, 0)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
cam.release()
