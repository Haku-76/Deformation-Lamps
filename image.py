# -*- coding: utf-8 -*-

from cv2 import cv2

# 静止画の読み込み
image = cv2.imread("static.png")

# 画像のサイズをを取得する
image_height = image.shape[0]
image_width = image.shape[1]
print(f"Image Height = {image_height}, Image Width = {image_width}")

# 画像のサイズを調整する
image = cv2.resize(image , (int(image_width*0.5), int(image_height*0.5)))

# YCbCr色空间に変化する
image_ycrcb = cv2.cvtColor(image,cv2.COLOR_BGR2YCrCb)
# Y	= 0.299R+0.587G+0.114B
# Cr = 0.500R-0.419G-0.081B
# Cb = -0.169R-0.332G+0.500B

# YCbCrチャンネルのy,cb,crの数値を取得する
y, cb, cr = cv2.split(image_ycrcb)

cv2.imshow("Static Image",image)
cv2.moveWindow("Static Image", 0, -100)

cv2.imshow("YCrCb Image",image_ycrcb)
cv2.moveWindow("YCrCb Image", image_width//2+10, -100)

cv2.imshow("Y Image",y)
cv2.moveWindow("Y Image", 0, image_height//2-40)

if cv2.waitKey(1) & 0xFF == ord("q"):
    cv2.destroyAllWindows()
