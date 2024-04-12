import cv2

print(cv2.__version__)

rows = int(input("How many rows do you want? "))
columns = int(input("and how many columns? "))

width = 640
height = 360

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
# cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
while True:
    _, frame = cam.read()
    frame = cv2.resize(frame, (int(width / columns), int(height / columns)))
    for row in range(0, rows):
        for column in range(0, columns):
            winName = "Window" + str(row) + " x " + str(column)
            cv2.imshow(winName, frame)
            cv2.moveWindow(
                winName, int(width / columns) * column, int(height / columns + 30) * row
            )
    if _:
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
cam.release()
