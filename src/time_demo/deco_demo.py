#使用 Decorator / Annotation 方式宣告
from schedule import every, repeat, run_pending, clear, get_jobs
from datetime import datetime
import time

@repeat(every(5).seconds)
def task1():
    print(f"這是任務  1 {datetime.now()}")

@repeat(every(2).seconds)
def task2():
    print(f"這是任務  2 {datetime.now()}")

@repeat(every(20).seconds.until("15:30"))
def task3():
    print(f"這是任務  3 {datetime.now()}")

@repeat(every(3).to(8).seconds)   #亂數 3~8 秒 後執行這任務
def task4():
    print(f"*** 這是亂數任務 4 {datetime.now()}")

@repeat(every(30).seconds)
def task5():
    clear()

while True:
    run_pending()
    print(f"job pool 是否有任務: {len(get_jobs())}")
    if len(get_jobs()) == 0:
        print("job pool 內已無任何任務可執行")
        break   #離開while迴圈，因為已無任務
    time.sleep(1)


print("程式結束")