#number parser

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90
}

while True:
    userinput = input("Type a number in text form: ").split()

    if "quit" in userinput:
        break

    current = 0
    total = 0
    unknown = []

    for word in userinput:
        if word in numbers:
            current += numbers[word]
        elif word == "hundred":
            current *= 100
        elif word == "thousand":
            total += current * 1000
            current = 0
        elif word == "million":
            total += current * 1000000
            current = 0
        elif word == "billion":
            total += current * 1000000000
            current = 0
        else:
            unknown.append(word)

    print(total + current)

    if unknown:
        print(f"unknown word detected {unknown}")
