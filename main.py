from src import Scheduler, apply_emergency, input_availability, input_days, Availability, Worker, Day
from typing import List

def collect_emergency(availability: Availability, days: List[Day]) -> None:
    """
    使用者輸入，收集請假資訊，直接修改 availability
    """
    workers = list(availability.keys())
    print(f"目前可用員工: {', '.join(workers)}")
    print(f"目前需排班日期:{', '.join(days)}")
    
    while True:
        unavailable_worker: str = input(
            "請輸入請假員工名稱(或 Enter 結束):"
        ).strip()

        # 未輸入則結束
        if not unavailable_worker:
            break

        # 找不到輸入的員工
        if unavailable_worker not in availability:
            print(f"找不到員工：{unavailable_worker} !!請重新輸入!!!")
            continue
        
        day: Day = input(
            f"請輸入 {unavailable_worker} 請假的日期（如 Mon):"
        ).strip()

        # 找不到輸入的日期
        if not day:
            print("日期不可為空!!")
            continue
        
        # 本來就不在該日上班
        if day not in availability[unavailable_worker]:
            print(f"{unavailable_worker} 本來就不能在 {day} 上班")
            continue

        apply_emergency(availability, unavailable_worker, day)
        print(f"已完成請假登記: {unavailable_worker} - {day} 休假")


def main():

    availability = input_availability("config/availability.json")
    days = input_days("config/days.json")
    priorities = input_days("config/priority.json")

    collect_emergency(availability, days)

    scheduler = Scheduler(availability, days, priorities)
    shift_schedule = scheduler.Action()

    if shift_schedule is None:
        print("無法排出合法班表...")
    else:
        print("排班結果：")
        for day, worker in shift_schedule.items():
            print(f"{day}: {worker}")

if __name__ == "__main__":
    main()
