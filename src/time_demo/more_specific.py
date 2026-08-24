import schedule
import time
from datetime import datetime


def task1(): 
    print(f"任務1 完成時間: {datetime.now()}") 


schedule.every(3).hours.do(task1)
schedule.every().hour().at(":15").do(task1) # 每小時的15分 (12:30 12:45分) 執行
schedule.every(4).hours().at(":15").do(task1)
schedule.every().day.at("12:30").do(task1)  # 每天的中午 12:30 分執行
schedule.every().wednesday.at("23:00").do(task1)
schedule.every().minute.at(":45")   #每分鐘的45秒 (12:30:45 12:31:45秒) 執行