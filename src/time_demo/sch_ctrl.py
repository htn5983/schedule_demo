import schedule
import time


def task1():
    print("hello!!")


job1 = schedule.every(10).seconds.do(task1)
job2 = schedule.every(20).seconds.do(task1)
 # 產生 job(任務) 放入排程池


while True:
    schedule.run_pending()  #檢查是否有等候中的任務
    print(f"job pool 是否有任務: {len(schedule.get_jobs())}")
    if len(schedule.get_jobs()) == 0:
        print("job pool 內已無任何任務可執行")
        break   #離開while迴圈，因為已無任務

    #清除所有任務
    schedule.clear()  #強制把所有任務清除
    time.sleep(1)


print("程式結束")