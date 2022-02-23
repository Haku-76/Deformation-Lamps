# -*- coding: utf-8 -*-

from cv2 import cv2
import numpy as np
import time

i = 0      # カウント変数

movie = cv2.VideoCapture("sample.mp4")

ret, bg = movie.read()

while True:

    ret, frame = movie.read()

    # フレームが取得できない場合はループを抜ける
    if not ret:
        print("No Frame")
        break

    # 差分の絶対値を計算
    mask = cv2.absdiff(frame, bg)

    mask_ycrcb = cv2.cvtColor(mask,cv2.COLOR_BGR2YCrCb)
    y, cb, cr = cv2.split(mask_ycrcb)

    cv2.imshow("frame",y)

    # 待機
    time.sleep(0.02)
    i += 1    # カウントを1増やす

    # 背景画像の更新（一定間隔）
    if(i > 5):
        ret, bg = movie.read()
        i = 0  # カウント変数の初期化

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

movie.release()
cv2.destroyAllWindows()
