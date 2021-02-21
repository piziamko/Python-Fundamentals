worker_1 = int(input())
worker_2 = int(input())
worker_3 = int(input())

people_waiting = int(input())
people_per_hour = worker_1 + worker_2 + worker_3
hours = 0

while people_waiting > 0:
    hours += 1
    people_waiting -= people_per_hour
    if hours % 4 == 0:
        people_waiting += people_per_hour

print(f"Time needed: {hours}h.")
