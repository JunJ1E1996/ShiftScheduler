from collections import defaultdict

#員工可上班日
availability = {
    "A": {"Mon", "Tue", "Wed"},
    "B": {"Mon", "Thu", "Fri"},
    "C": {"Tue", "Wed", "Thu"},
    "D": {"Tue", "Fri"}
}

Days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
MAX_DAYS_PER_PERSON = 2



# 排班主 function
def schedule_shifts(availability):
    assigned = {}  # day -> worker
    count = defaultdict(int)  # record count of assigned days of each workers

    def find_daily_shift(day_idx):
        if day_idx == len(Days): # finish shifts
            return True
        
        day = Days[day_idx]
        cadidates = [
            w for w in availability
            if day in availability[w]
        ]

        for c in cadidates:
            if count[c] >= MAX_DAYS_PER_PERSON:
                continue # reach the limit of day count

            assigned[day] = c # 把該日嘗試 assign 給 c
            count[c] += 1

            if find_daily_shift(day_idx + 1): # 嘗試往下排
                return True
            
            # 回溯（撤銷剛剛的嘗試）
            count[c] -= 1
            del assigned[day]
        
        return False
    
    
    res = find_daily_shift(0)
    if res:
        return assigned
    else:
        return None
    
def apply_emergency(availability, worker, day):
    new_availability = {k:set(v) for k, v in availability.items()}
    if day in new_availability[worker]:
        new_availability[worker].remove(day)
    return new_availability


print("第一次排班：")
result = schedule_shifts(availability)
print(result)

print("第二次排班：")
new_av = apply_emergency(availability, "A", "Mon")
result = schedule_shifts(new_av)
print(result)



