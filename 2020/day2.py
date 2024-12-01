import re

with open('./2020/input/day2.txt', 'r') as file:
    file = [re.split('-| |:', x.strip()) for x in file]

def part1():
    # Obj: Find how many passwords are valid according to their policies
    valid_pass = 0
    for i in range(len(file)):
        min_num = int(file[i][0])
        max_num = int(file[i][1])
        letter = file[i][2]
        password = file[i][4]
        actual = password.count(letter)
        if min_num <= actual <= max_num:
            valid_pass += 1
    return valid_pass

def part2():
    # Obj: Find how many passwords are valid according to their policies
    valid_pass = 0
    for i in range(len(file)):
        valid_pos1 = int(file[i][0])
        valid_pos2 = int(file[i][1])
        letter = file[i][2]
        password = file[i][4]
        if password[valid_pos1 -1] == letter and password[valid_pos2 -1] != letter or password[valid_pos2 -1] == letter and password[valid_pos1 -1] != letter:
            valid_pass += 1
    return valid_pass



print(f"Answer to part 1 is: {part1()}")
print(f"Answer to part 2 is: {part2()}")