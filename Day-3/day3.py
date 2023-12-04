def getLines(lineStart, lineEnd, currentLine):
    with open('input.txt', 'r', newline='') as values:
        lines = {}
        for lineId, line in enumerate(values):
            line = line.strip()
            if lineStart == lineId:
                lines[lineId] = line
            if lineEnd == lineId:
                lines[lineId] = line
            if currentLine == lineId:
                lines[lineId] = line
        # print("your lines are: ", lines)
        return(lines)
def checkBoundaries(part):
    print(part)
    lines = getLines(part['checkLinePrior'], part['checkLineAfter'], part['currentLine'])
    for line in lines:
        # if part['checkLinePrior'] == line or part['checkLineAfter'] == line or part['currentLine'] == line:
        print(line, lines[line])

    # Current Line
    # check immediately prior to the part
    print('Checking current line')
    priorChar = lines[part['currentLine']][part['checkIndexStart']]
    followingChar = lines[part['currentLine']][part['checkIndexEnd']]
    # print(priorChar, followingChar)

    if not priorChar.isalpha() and not priorChar.isdigit() and not priorChar == '.':
        # print('HEY LISTEN', priorChar)
        return(True)
    if not followingChar.isalpha() and not followingChar.isdigit() and not followingChar == '.':
        # print('HEY LISTEN', followingChar)
        return(True)
        # DO SOMETHING BECAUSE IT'S VALID OMG

    # Prior Line
    # make sure prior line is not current line
    if part['checkLinePrior'] != part['currentLine']:
        print("CHECKING PRIOR LINE")
        indexLength = part['checkIndexEnd'] - part['checkIndexStart'] + 1
        # print(indexLength)
        for position in range(0, indexLength):
            checkIndex = part['checkIndexStart'] + position
            char = lines[part['checkLinePrior']][checkIndex]
            if not char.isalpha() and not char.isdigit() and not char == '.':
                # print(char)
                # print("HEY LOOK FOUND SOMETHING")
                return(True)
    else:
        print('No prior line')

    # Next Line
    # make sure next line exists
    try:
        # make sure following line is not current line
        if part['checkLineAfter'] != part['currentLine']:
            print("CHECKING NEXT LINE")
            indexLength = part['checkIndexEnd'] - part['checkIndexStart'] + 1
            # print(indexLength)
            for position in range(0, indexLength):
                checkIndex = part['checkIndexStart'] + position
                char = lines[part['checkLineAfter']][checkIndex]
                if not char.isalpha() and not char.isdigit() and not char == '.':
                    # print(char)
                    # print("HEY LOOK FOUND SOMETHING")
                    return(True)
    except:
        print("no more lines")

def defineBoundaries(parts, line, lineId):
    lineValue = 0
    for part in parts:
        print(part)
        if part['indexStart'] != 0:
            checkIndexStart = part['indexStart'] - 1
        else:
            checkIndexStart = part['indexStart']
        if part['indexEnd'] != len(line) - 1:
            checkIndexEnd = part['indexEnd'] + 1
        else:
            checkIndexEnd = part['indexEnd']
        if part['lineID'] != 0:
            checkLinePrior = lineId - 1
        else:
            checkLinePrior = 0
        checkLineAfter = lineId + 1

        checkPart = {
            "part": part['part'],
            "checkIndexStart": checkIndexStart,
            "checkIndexEnd": checkIndexEnd,
            "checkLinePrior": checkLinePrior,
            "checkLineAfter": checkLineAfter,
            "currentLine": lineId
        }

        check = checkBoundaries(checkPart)
        if check:
            print("Valid part: ", int(part['part']))
            lineValue += int(part['part'])
            print("New line value: ", lineValue)
    return(lineValue)


def partOne():
    totalValue = 0
    with open('input.txt', 'r', newline='') as values:
        for id, line in enumerate(values):
            line = line.strip()
            print(id, line)
            # find parts in the current line

            parts = []

            # partNumber = {
            #     "part": '',
            #     "indexStart": '',
            #     "indexEnd": '',
            #     "lineID": ''
            # }

            indexStart = ''
            indexEnd = ''
            part = ''

            for position, character in enumerate(line):
                # print(position, character)
                # print('Current parts list: ', parts)
                if character.isdigit():
                    if indexStart == '':
                        indexStart = position
                    indexEnd = position
                    part += str(character)
                    # print("Part Number: ", part)
                    if len(line) == (position + 1):
                        partNumber = {
                            "part": part,
                            "indexStart": indexStart,
                            "indexEnd": indexEnd,
                            "lineID": id
                        }
                        parts.append(partNumber)
                        # print("reached end of line. parts list: ", parts)

                else:
                    if part == '':
                        # print('no digit here, but heres a parts list: ', parts)
                        # print('no part found yet')
                        continue
                    if part != '':
                        # print(part)
                        partNumber = {
                            "part": part,
                            "indexStart": indexStart,
                            "indexEnd": indexEnd,
                            "lineID": id
                        }
                        parts.append(partNumber)
                        # print("new parts list: ", parts)
                        indexStart = ''
                        indexEnd = ''
                        part = ''

            # print(parts)
            lineValue = defineBoundaries(parts, line, id)
            print("TOTAL LINE VALUE: ", lineValue)
            totalValue += lineValue
    print(totalValue)
partOne()