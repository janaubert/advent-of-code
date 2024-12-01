import re

with open('./2020/input/day4.txt', 'r') as file:
    input_text = file.read()

    # Split on double newlines, then join lines in each section
    sections = [section.replace("\n", " ") for section in input_text.strip().split("\n\n")]

    test = list(re.split(':| ', x) for x in sections)

    required = {
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid"
    }

# En funksjon for å validere om noe faktisk er innenfor en regel
# Ny funksjon for å bruke svaret fra første funksjon

def is_valid():

    valid_passports = []
    for i in range(len(test)):
        counter = 0
        for req in required:
            if req in test[i]:
                counter += 1
        if counter == 7:
            #print(test[i], req)
            valid_passports.append(test[i])
    return valid_passports

def part_one():
    
    return len(is_valid())

# Define the conditions dictionary as before
CONDITIONS = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: (
        (x.endswith("cm") and 150 <= int(x[:-2]) <= 193) or
        (x.endswith("in") and 59 <= int(x[:-2]) <= 76)
    ),
    "hcl": lambda x: bool(re.match(r"^#[0-9a-f]{6}$", x)),
    "ecl": lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    "pid": lambda x: bool(re.match(r"^\d{9}$", x)),
    "cid": lambda x: True,  # `cid` is optional
}

def is_valid_passport(passport, conditions):
    # Convert the passport list to a dictionary (keys are odd indices, values are even indices)
    passport_dict = {passport[i]: passport[i + 1] for i in range(0, len(passport), 2)}
    
    # Check if all required keys are present and satisfy the conditions
    for key, value in passport_dict.items():
        if key in conditions:
            # If the value does not satisfy the condition, return False
            if not conditions[key](str(value)):
                return False
    # If all conditions are satisfied
    return True

def count_valid_passports(input_data, conditions):
    valid_count = 0
    for passport in input_data:
        if is_valid_passport(passport, conditions):
            valid_count += 1
    return valid_count

# Example input
input_data = is_valid()

# Count valid passports
valid_passports_count = count_valid_passports(input_data, CONDITIONS)


print(f"Part one: {part_one()}")
print(f"Part two: {valid_passports_count}")