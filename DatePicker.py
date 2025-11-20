import sys
weekString = []
for i in range(7):
    weekString[i] = input()
days,hours = map(int,input().split())

week = []

for day in range(7):
    for hour in range(24):
        if weekString[day][hour] == "x":
            week[day][hour] = 0
        else:
            week[day][hour] = 1

operations =pow(days,7)

besteStunden = []
for hour in range(24):
    besteStunden[hour] = sum(week[0:7][hour])

besteStunden.sort()



