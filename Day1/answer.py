f = open("input.txt", "r")
max_num = float('-inf')
curr_num = 0
for line in f:
    line = line.strip()
    if(line == ""):
        curr_num = 0
    else:
        curr_num += int(line)
    
    if curr_num > max_num:
        max_num = curr_num

print(max_num)