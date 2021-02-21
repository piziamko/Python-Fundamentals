first = int(input())
second = int(input())
third = int(input())
all_students = int(input())
all_served_employee_ = first + second + third
hours = 0
while all_students > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    all_students -= all_served_employee_


print(hours)
