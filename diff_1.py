# -*- coding: utf-8 -*-

from cv2 import cv2
import numpy as np

movie = cv2.VideoCapture("sample.mp4")

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

while True:

    ret, frame = movie.read()

    # フレームが取得できない場合はループを抜ける
    if not ret:
        print("No Frame")
        break

    fgmask = fgbg.apply(frame)

    cv2.imshow("frame",fgmask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

movie.release()
cv2.destroyAllWindows()
