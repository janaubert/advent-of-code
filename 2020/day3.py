with open('./2020/input/day3.txt', 'r') as file:
    file = [x.strip().split(' ') for x in file]

    data = []
    for elem in range(len(file)):
        for letter in file[elem]:
            data.append(letter * 1000)

def part1():
    # Obj:
    score = 0
    position = 0
    for i in range(len(data)):
        # print(data[i][position])
        if data[i][position] == '#':
            score += 1
        position += 3
    return score

def part2():
    # Obj:
    score_1 = 0
    score_2 = 0
    score_3 = 0
    score_4 = 0
    score_5 = 0
    route_1 = 0
    route_2 = 0
    route_3 = 0
    route_4 = 0
    route_5 = 0
    for i in range(len(data)):
        # print(data[i][position])
        if data[i][route_1] == '#':
            score_1 += 1
        if data[i][route_2] == '#':
            score_2 += 1
        if data[i][route_3] == '#':
            score_3 += 1
        if data[i][route_4] == '#':
            score_4 += 1
        route_1 += 1
        route_2 += 3
        route_3 += 5
        route_4 += 7
    for i in range(len(data)):
        print(data[i][route_5], i)
        if i % 2 != 0:
            route_5 += 0
        elif data[i][route_5] == '#' and i % 2 == 0:
            score_5 += 1
            route_5 += 1
        elif data[i][route_5] == '.' and i % 2 == 0:
            score_5 += 0
            route_5 += 1
    return score_1,score_2,score_3,score_4,score_5, score_1*score_2*score_3*score_4*score_5

#Right 1, down 1.
#Right 3, down 1. (This is the slope you already checked.)
#Right 5, down 1.
#Right 7, down 1.
#Right 1, down 2.


print(f"Answer to part 1 is: {part1()}")
print(f"Answer to part 2 is: {part2()}")