import time
from datetime import datetime

#透過 time 可以在固定頻率執行應用程式

def task(): 
    print(f"現在時間: {datetime.now()}")


while True:
    # 檢查現在是否是 11:35:21秒 ； 是-->執行 task() ； 不是就跳過
    task()
    time.sleep(1)   # 在迴圈中每執行一次task後就停頓幾秒鐘