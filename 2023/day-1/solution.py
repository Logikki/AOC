import re

ENUM_DIGITS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def sumOfValues(data: str) -> int:
    lines = [[int(char) for char in lines if char.isdigit()] for lines in data if lines != "\n"]
    listOfWantedValues = [[numbers[0], numbers[-1]] for numbers in lines] 
    valuesAsInt = [int("".join(map(str, value))) for value in listOfWantedValues]
    return(sum(valuesAsInt))

def sumOfValuesIncludingWords(data: str) -> int:
    for i, line in enumerate(data):
        data[i] = findAndReplaceNumb(line)
    return sumOfValues(data)

def findAndReplaceNumb(line: str) -> str:
    numbersAsDigit = [i for i in line]
    
    #find all word matches. Append digit to start of reg match
    for digit, word in enumerate(ENUM_DIGITS):
        matches = re.finditer(word, line)
        for match in matches:
            numbersAsDigit[match.start()] = str(digit + 1)

    return ("".join(numbersAsDigit))

def main():
    fr = open("data.txt", "r")
    data = fr.readlines()
    fr.close
    
    print("1 star answer: " + str(sumOfValues(data)))
    print("2 star answer: " + str(sumOfValuesIncludingWords(data)))

if __name__ == "__main__":
    main()
    