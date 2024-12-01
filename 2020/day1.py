with open('./2020/input/day1.txt', 'r') as file:
    file = [int(x.strip()) for x in file]

def part1():
    # Obj: Find the two entries that sums up to 2020, and then mulitply these two numbers together.
    index_iter = 0
    
    while index_iter < len(file):
        for num in range(len(file)):
            if file[index_iter] + file[num] == 2020:
                return file[index_iter] * file[num]
                break
        index_iter +=1

def part2():
    # Obj: Find the THREE entries that sums up to 2020, and then mulitply these numbers together.
    index_iter = 0
    second_iter = 1
    
    while index_iter < len(file)-2:
        for num in range(len(file)):
            for j in range(len(file)):
                if file[index_iter] + file[num] + file[j] == 2020:
                    return file[index_iter] * file[num] * file[j]
                    break
            num +=1
        index_iter +=1

print(f"Answer to part 1 is: {part1()}")
print(f"Answer to part 2 is: {part2()}")