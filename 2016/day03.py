data = []
with open('day03.data', 'r') as myfile:
    data=[[int(val) for val in line.strip().split()] for line in myfile]

goods = 0
for line in data:
    if line[0] < (line[1] + line[2]) and line[1] < (line[0] + line[2]) and line[2] < (line[1] + line[0]): 
        goods += 1

print goods