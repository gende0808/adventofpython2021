day1a, day1b = 0, 0
with open("Day1.txt") as txtfile:
    inputArray = list(map(int, txtfile.read().split()))
for num in range(len(inputArray) - 1):
    if inputArray[num] < inputArray[num + 1]:
        day1a += 1
for num in range(len(inputArray) - 2):
    if sum(inputArray[num:num+3]) < sum(inputArray[num+1:num+4]):
        day1b += 1
print(f"day1.1: {day1a} day1.2: {day1b}")