import picamera
import os
from time import sleep
import datetime
from PIL import Image
import numpy as np


dt_now = datetime.datetime.now()
timestamp = dt_now.strftime('%Y%m%d_%H%M%S')

# 保存ディレクトリを設定
image_dir = '/home/pi/fluorescence/picture'
count_dir = '/home/pi/fluorescence/count'


# カメラを初期化
camera = picamera.PiCamera()
print("start camera")
# カメラの設定
camera.resolution = (3280, 2464)  
camera.shutter_speed = 1000000  # シャッタースピード1秒
camera.start_preview()  # カメラのプレビューを開始
sleep(2)  


#写真パート--------------------------------------------------------------
# 写真を撮影して保存
image_path = os.path.join(image_dir, f'{timestamp}_image.jpg')
camera.capture(image_path)
print(f"Image saved at: {image_path}")

# カメラリソースを解放
camera.close()
print("finish camera")
#--------------------------------------------------------------



#カウント値保存パート--------------------------------------------------------------
# 画像を読み込み
print("change to count_value・・・")
image = Image.open(image_path)
image = image.convert('L')  # グレースケールに変換

# ピクセルごとの明るさを取得
brightness_array = np.array(image)
print("finish change to count_value")

# 明るさのカウント値をファイルに保存
count_path = os.path.join(count_dir, f'{timestamp}_brightness_values.txt')
np.savetxt(count_path, brightness_array, fmt='%d')
print(f"Brightness values saved at: {count_path}")
#--------------------------------------------------------------