import cv2
import numpy as np

boardSize = int(input("What size is your board? "))
numSquared = int(input("and how many squares? "))
squareSize = int(boardSize / numSquared)

darkColor = (0, 0, 0)
lightColor = (175, 175, 175)
nowColor = darkColor

while True:
    x = np.zeros([boardSize, boardSize, 3], dtype=np.uint8)

    for row in range(0, numSquared):
        for column in range(0, numSquared):
            x[
                squareSize * row : squareSize * (row + 1),
                squareSize * column : squareSize * (column + 1),
            ] = nowColor
            if nowColor == darkColor:
                nowColor = lightColor
            else:
                nowColor = darkColor
        if nowColor == darkColor:
            nowColor = lightColor
        else:
            nowColor = darkColor

    cv2.imshow("My checkerboard", x)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
