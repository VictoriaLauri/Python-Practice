import datetime

day = datetime.date.fromisoformat(input("Date: "))

def is_workday(day):
    if day.weekday() == 5 or day.weekday() == 6:
        return False
    return True

if is_workday(day):
    print("Workday")
else:
    print("Weekend")
