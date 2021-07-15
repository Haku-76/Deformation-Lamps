# -*- coding: utf-8 -*-

from cv2 import cv2
import numpy as np
import time

i = 0      # カウント変数

# 静止画の読み込み
# image = cv2.imread("static_1.png")
image = cv2.imread("static_2.png")

# 画像のサイズを取得する
image_height = image.shape[0]
image_width = image.shape[1]
print(f"Image Height = {image_height}, Image Width = {image_width}")

# 画像のサイズを調整する
image = cv2.resize(image, (int(image_width*0.5), int(image_height*0.5)))

cv2.imshow("Static Image",image)
cv2.moveWindow("Static Image", 0, -100)

# YCbCr色空间に変換する
image_ycrcb = cv2.cvtColor(image,cv2.COLOR_BGR2YCrCb)
# Y	= 0.299R+0.587G+0.114B
# Cr = 0.500R-0.419G-0.081B
# Cb = -0.169R-0.332G+0.500B

# YCbCrチャンネルのy,cb,crの数値を取得する
image_y, image_cb, image_cr = cv2.split(image_ycrcb)

cv2.imshow("Y Image",image_y)
cv2.moveWindow("Y Image", image_width//2+10, -100)

# 動画を読み込む
# movie = cv2.VideoCapture("movie_1.mp4")
movie = cv2.VideoCapture("movie_2.mp4")

# 差分用の背景を準備する
ret, bg = movie.read()

# 動画ファイルの設定
fps = int(movie.get(cv2.CAP_PROP_FPS)) # 動画のFPSを取得する
movie_height = int(movie.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 動画の縦幅を取得する
movie_width = int(movie.get(cv2.CAP_PROP_FRAME_WIDTH)) # 動画の横幅を取得する
print(f"Movie FPS = {fps}")
print(f"Movie Height = {movie_height}, Movie Width = {movie_width}")

# ファイルからフレームを1枚ずつ取得して動画処理する
while True:

    ret, frame = movie.read() # フレームを取得する

    # フレームが取得できない場合はループを抜ける
    if not ret:
        print("No Frame")
        break
    
    # 画像のサイズをを取得する
    # frame_height = image.shape[0]
    # frame_width = image.shape[1]
    # frame = cv2.resize(frame , (int(frame_width*0.5), int(frame_height*0.5)))

    # 差分の絶対値を計算
    mask = cv2.absdiff(frame, bg)

    mask_ycrcb = cv2.cvtColor(mask,cv2.COLOR_BGR2YCrCb)
    mask_y, mask_cb, mask_cr = cv2.split(mask_ycrcb)

    cv2.namedWindow("Diff Y Frame", 0)
    cv2.resizeWindow("Diff Y Frame", int(movie_width*0.5), int(movie_height*0.5))
    cv2.imshow("Diff Y Frame", mask_y)
    cv2.moveWindow("Diff Y Frame", 0, movie_height//2-40)

    # カウントを1増やす
    i += 1    

    # 背景画像の更新
    if(i > 2):
        ret, bg = movie.read()
        i = 0  # カウント変数の初期化

    # 背景と前景のサイズを統一する
    image = cv2.resize(image,(640,360))
    frame = cv2.resize(frame,(640,360))

    # 背景と前景を融合する
    perform = cv2.addWeighted(image,0.5,frame,0.5,2)
    cv2.imshow("Perform",perform)
    cv2.moveWindow("Perform", movie_width//2+10, movie_height//2-40)
    
    # frame_ycrcb = cv2.cvtColor(frame,cv2.COLOR_BGR2YCrCb)
    # frame_y, frame_cb, frame_cr = cv2.split(frame_ycrcb)

    # cv2.namedWindow("Y Frame", 0)
    # cv2.resizeWindow("Y Frame", int(movie_width*0.5), int(movie_height*0.5))
    # cv2.imshow("Y Frame", y)
    # cv2.moveWindow("Y Frame", movie_width//2+10, movie_height//2-40)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

movie.release()
cv2.destroyAllWindows()
