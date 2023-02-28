#! usr/bin/env python3
n, m = map(int, input().split())

arr = []

currentwinner = -1
currentnumber = 0

def sumarr(array):
    summing = 0
    for k in array:
        summing += k
    return summing

for i in range(n):
    number = sumarr(list(map(int, input().split())))
    if currentwinner == -1 or number > currentnumber:
        currentnumber = number
        currentwinner = i

print(currentwinner+1)