import cv2
import numpy as np

# frame = np.zeros([5, 5, 3], dtype=np.uint8)

# frame[0:2, 0:5] = 100

# print(frame)

while True:
    frame = np.zeros([250, 250, 3], dtype=np.uint8)
    # Make red
    frame[:, :] = (0, 0, 255)
    # Left half green
    frame[:, :125] = (0, 255, 0)
    cv2.imshow("My window", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
