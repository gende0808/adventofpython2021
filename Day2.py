input = [x for x in open('Day2.txt').read().strip().split('\n')]
y, x, y2, aim = 0,0,0,0,0
for item in input:
    num = item.split(' ')[1]
    if "forward" in item:
        x += int(num)
        y2 += aim * int(num)
    if "up" in item:
        y += int(num)
        aim += int(num)
    if "down" in item:
        aim -= int(num)
        y -= int(num)
print(x * y)
print(y2 * x)