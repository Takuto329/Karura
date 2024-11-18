import picamera
from time import sleep
from PIL import Image
import numpy as np

# カメラを初期化
camera = picamera.PiCamera()

try:
    # カメラの設定
    camera.resolution = (1024, 768)  # 解像度を1024x768に設定
    camera.start_preview()  # カメラのプレビューを開始
    
    # プレビューを表示するために2秒待機
    sleep(2)  # プレビューが表示されるのを待つ
    
    # 写真を撮影して保存
    image_path = '/home/pi/image.jpg'  # 画像の保存パスを設定
    camera.capture(image_path)  # 画像をキャプチャして指定したパスに保存
    
    # 画像を読み込み
    image = Image.open(image_path)  # 保存した画像を開く
    image = image.convert('L')  # 画像をグレースケールに変換
    
    # ピクセルごとの明るさを取得
    brightness_array = np.array(image)  # 画像をNumPy配列に変換
    
    # 明るさのカウント値をファイルに保存
    np.savetxt('/home/pi/brightness_values.txt', brightness_array, fmt='%d')  # 明るさの値をテキストファイルに保存
finally:
    # カメラをクリーンアップ
    camera.close()  # カメラリソースを解放