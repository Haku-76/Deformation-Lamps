# -*- coding: utf-8 -*-

from cv2 import cv2

# 動画を読み込む
movie = cv2.VideoCapture("sample.mp4")

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

    # フレームのサイズを調整する
    cv2.namedWindow("Original Frame", 0)
    cv2.resizeWindow("Original Frame", int(movie_width*0.5), int(movie_height*0.5))
    cv2.imshow("Original Frame", frame)

    frame_ycrcb = cv2.cvtColor(frame,cv2.COLOR_BGR2YCrCb)
    y, cb, cr = cv2.split(frame_ycrcb)

    cv2.namedWindow("Y Frame", 0)
    cv2.resizeWindow("Y Frame", int(movie_width*0.5), int(movie_height*0.5))
    cv2.imshow("Y Frame", y)
    cv2.moveWindow("Y Frame", movie_width//2+10, -100)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

movie.release()
cv2.destroyAllWindows()