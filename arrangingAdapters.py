import sys

    
numchargers,numSockets = map(int,input().split())
chargers = [int(i) for i in input().split()]


#case for only 2 sockets and sorting
chargers.sort()

if numSockets <= 2:
    print(min(numchargers,numSockets))

#puts the biggest one on the 
c1 = chargers.pop(-1)
c2 = chargers.pop(-1)
numSockets = numSockets-2

left = 0
right = len(chargers)
Position = 0

while True:
    Position = (left + right)//2

    rest0,rest1,rest2 = [],[],[]
    for i in range(Position):
        if chargers[i]%3 ==0:
            rest0.append(chargers[i])
        if chargers[i]%3 ==1:
            rest1.append(chargers[i])
        if chargers[i]%3 ==2:
            rest2.append(chargers[i])
    lenght = sum(rest0)
    minFromRest = min(len(rest1),len(rest2))
    lenght += sum(rest1[:minFromRest])+ sum(rest2[:minFromRest])
    if minFromRest == len(rest1):
        for j in range(minFromRest,len(rest2)):
            lenght += rest2[j]+1
    elif minFromRest == len(rest2):
        ungerade =  (len(rest1)-minFromRest)%2!=0
        if ungerade:
            lenght += rest1.pop()+2
        for j in range(minFromRest,len(rest1),2):
            lenght += rest1[j]+rest1[j+1]+1
    neededSockets = lenght/3

    if numSockets >= neededSockets:
        left = Position + 1
    else:
        right = Position
        Position -= 1
    
    if left==right:
        break

positionLast = (left + right)//2

rest0,rest1,rest2 = [],[],[]
for i in range(positionLast):
    if chargers[i]%3 ==0:
        rest0.append(chargers[i])
    if chargers[i]%3 ==1:
        rest1.append(chargers[i])
    if chargers[i]%3 ==2:
        rest2.append(chargers[i])
lenght = sum(rest0)
minFromRest = min(len(rest1),len(rest2))
lenght += sum(rest1[:minFromRest])+ sum(rest2[:minFromRest])
if minFromRest == len(rest1):
    for j in range(minFromRest,len(rest2)):
        lenght += rest2[j]+1
elif minFromRest == len(rest2):
    ungerade =  (len(rest1)-minFromRest)%2!=0
    if ungerade:
        lenght += rest1.pop()+2
    for j in range(minFromRest,len(rest1),2):
        lenght += rest1[j]+rest1[j+1]+1
neededSockets = lenght/3

if numSockets >= neededSockets:
    print(positionLast+2)
else:
    print(Position+2)
