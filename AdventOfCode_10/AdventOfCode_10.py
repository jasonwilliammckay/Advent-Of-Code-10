# Per http://adventofcode.com/day/10

iterations = 40
startingInput = "1321131112"

def main():
    input = startingInput
    
    if (len(startingInput) > 0):        # check for valid input
        for i in range(0, iterations):
            input = seeAndSay(input)

    print "For the input \"{0}\", across {1} iterations, the length of the result is {2:,}.".format(startingInput, iterations, len(input))

def addToList(list, item1, item2):
    list.append(str(item1))
    list.append(str(item2))
    return list

def seeAndSay(input):
    charName = input[0]         # pre-load the first character in the string to be checked    
    charLen = 1
    resultList = [];

    for i in range (1, len(input)):
        if (input[i] == charName):
            charLen += 1
        else:
            resultList = addToList(resultList, charLen, charName)
            charName = input[i]
            charLen = 1

    resultList = addToList(resultList, charLen, charName)   # add the final substring to the list
    return ''.join(resultList)
    
main()