with open('./2020/input/day5.txt', 'r') as file:
    input_text = [x.strip() for x in file]

def find_row():
    # F = keep the lower half
    # B = keep the upper half
    upper = 128
    mid = 64
    lower = 0
    for letter in seat:
        if letter == 'F':
            upper = upper - mid
            mid = mid / 2
        elif letter == 'B':
            lower = lower + mid
            mid = mid / 2
    return lower

def find_column():
    # F = keep the lower half
    # B = keep the upper half
    upper = 8
    mid = 4
    lower = 0
    for letter in seat:
        if letter == 'L':
            upper = upper - mid
            mid = mid / 2
        elif letter == 'R':
            lower = lower + mid
            mid = mid / 2
    return lower


lst = []
for seat in input_text:
    lst.append(int(find_row()) * 8 + int(find_column()))
print(max(lst))

def part_one():
    pass


def part_two():    
    s_lst = sorted(lst)
    for i in range(len(s_lst)-1):
        if s_lst[i+1] - s_lst[i] != 1:
            print(s_lst[i+1], s_lst[i]) 


print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

