# Per http://adventofcode.com/day/10

startingInput = "1321131112"
iterations = 50

def main():
    input = startingInput
    i = 0

    while (i < iterations):
        input = seeAndSay(input)
        i += 1

    print "For the input {0}, across {1} iterations, the length of the result is {2:,}.".format(startingInput, iterations, len(input))

def seeAndSay(input):

    fullString = ""
    charName = input[0]
    charLen = 1
    i = 1;
    x = [];

    while (i < len(input)):

        if (input[i] == charName):
            charLen += 1

        else:
            x.append(str(charLen))
            x.append(str(charName))
            charName = input[i]
            charLen = 1

        i += 1
    
    x.append(str(charLen))
    x.append(str(charName))
    fullString = "".join(x)
    return fullString
    
main()