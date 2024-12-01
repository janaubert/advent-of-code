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
    for i in range(len(lst_one)):
        for j in range(len(lst_two)):
            if lst_one[i] in lst_two:
                print(lst_one[i], lst_two[j])


print(part_one())
print(part_two())
