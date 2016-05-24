# Per http://adventofcode.com/day/10

iterations = 40
startingInput = "1321131112"

def main():
    input = startingInput
    
    if (len(startingInput) > 0):
        for i in range(0, iterations):
            input = seeAndSay(input)

    print "For the input \"{0}\", across {1} iterations, the length of the result is {2:,}.".format(startingInput, iterations, len(input))

def seeAndSay(input):

    charName = input[0]
    charLen = 1
    resultList = [];

    for i in range (1, len(input)):

        if (input[i] == charName):
            charLen += 1

        else:
            resultList.append(str(charLen))
            resultList.append(str(charName))
            charName = input[i]
            charLen = 1
    
    resultList.append(str(charLen))
    resultList.append(str(charName))
    return "".join(resultList)
    
main()