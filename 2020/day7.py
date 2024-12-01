with open('./2020/input/day7.txt', 'r') as file:
    input_text = [x.strip() for x in file]
    #print(input_text)
    test = [x.replace("bags", "bag").split("contain") for x in input_text]
    #print(test)

def part_one():
    leads = []
    for i in range(len(test)):
        if " shiny gold bag" in test[i][1]:
            #print(test[i])
            leads.append(" " + test[i][0].strip())
    print(leads)
    counter = 0
    answer = []
    for sentence in range(len(input_text)):
        for lead in leads:
            if " shiny gold bag" in input_text[sentence] or lead in input_text[sentence]:
                counter += 1
                #print(input_text[sentence], lead, sentence)
                if input_text[sentence] not in answer:
                    answer.append(sentence)
                    #print(input_text[sentence], lead, sentence)
                #sentence +=1
    return counter, len(set(answer)), set(answer)

def part_two():
    pass

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")