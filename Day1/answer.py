f = open("input.txt", "r")
max_nums = set()
max_nums.add(-1)
max_nums.add(-2)
max_nums.add(-3)
curr_num = 0
for line in f:
    line = line.strip()
    if(line == ""):
        for amnt in max_nums:
            if curr_num > amnt:
                max_nums.remove(amnt)
                max_nums.add(curr_num)
                break
        curr_num = 0
    else:
        curr_num += int(line)
    

print(sum(max_nums))