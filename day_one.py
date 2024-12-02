with open('../ADVENT OF CODE/2024/input/day_one.txt') as file:
    f = [x.strip().split("   ") for x in file]
    #print(f)

    lst_one = []
    lst_two = []
def part_one():
    for i in range(len(f)):
        lst_one.append(int(f[i][0]))
        lst_two.append(int(f[i][1]))
    lst_one_s = sorted(lst_one)
    lst_two_s = sorted(lst_two)
    
    counter = 0
    for i in range(len(lst_one_s)):
        counter += abs(lst_one_s[i] - lst_two_s[i])
    return counter
    

def part_two():
    answer = []
    for num in lst_one:
        if num in lst_two:
            answer.append(int(num) * int(lst_two.count(num)))
    return sum(answer)

print(part_one())
print(part_two())
