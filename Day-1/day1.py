def partOne():
    totalValue = 0
    with open('input.txt', 'r', newline='') as values:
        for value in values:
            value = value.strip()
            # print(value)
            digits = []
            for char in value:
                # print('Character: ', char)
                if char.isdigit():
                    # print(char)
                    digits.append(int(char))
            # print(digits)
            if len(digits) == 1:
                lineValue = int(str(digits[0])+str(digits[0]))
                # print('Line Value: ', lineValue)
                totalValue += lineValue
            if len(digits) > 1:
                lineValue = int(str(digits[0])+str(digits[len(digits)-1]))
                # print('Line Value: ', lineValue)
                totalValue += lineValue

    print("Part One Answer: ", totalValue)

partOne()

def partTwo():
    totalValue = 0
    numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    with open('input.txt', 'r', newline='') as values:
        for value in values:
            value = value.strip()
            # print(value)

            first = 0
            last = 0

            while first == 0:
                word = ''
                length = len(value)
                while length >= 1:
                    # print("Length: ", length)
                    index = len(value) - length
                    char = value[index]
                    # print(char)
                    if char.isdigit():
                        first = char
                        length = 0
                    if char.isalpha():
                        word += char
                        length -= 1
                        # print("word: ", word)
                        for number in numbers:
                            r = word.find(number)
                            if r >= 0:
                                # print("found ", numbers[number])
                                first = str(numbers[number])
                                length = 0
                    if first != 0:
                        # print("first number: ", first)
                        continue
            while last == 0:
                word = ''
                length = len(value) - 1
                while length >= 1:
                    # print("Length: ", length)
                    index = length
                    char = value[index]
                    # print(char)
                    if char.isdigit():
                        last = char
                        length = 0
                    if char.isalpha():
                        word = char + word
                        length -= 1
                        # print("word: ", word)
                        for number in numbers:
                            r = word.find(number)
                            if r >= 0:
                                # print("found ", numbers[number])
                                last = str(numbers[number])
                                length = 0
                    if last != 0:
                        # print("last number: ", last)
                        continue
                else:
                    if last == 0:
                        last = first
            lineValue = int(str(first) + str(last))
            # print(value, lineValue)
            totalValue += lineValue
    print("Part Two Answer: ", totalValue)

partTwo()