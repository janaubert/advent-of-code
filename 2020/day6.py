with open('./2020/input/day6.txt', 'r') as file:
    input_text = file.read()
    
    lines = [x.strip().replace('\n', "") for x in input_text.split('\n\n')]
    line = [x.strip().split('\n') for x in input_text.split('\n\n')]
    #print(line)

def part_one():
    yesses = []
    for line in lines:
        answers = []
        for letter in line:
            if letter not in answers:
                answers.append(letter)
        yesses.append(len(answers))
    return sum(yesses)

def part_two():
    counter = 0
    for group in line:
        answers = []
        for person in group:
            answers.append(person)
        persons = len(answers)
        res = "".join([str(item) for item in answers])
        garbage = []
        for letter in res:
            if letter in garbage:
                continue
            if res.count(letter) >= persons:
                counter += 1
                garbage.append(letter)
    return counter

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")