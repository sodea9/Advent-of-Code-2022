#Advent of Code - Day 3
#Sean O'Dea

#Part 1 Functions

def construct_list(input):
    list = input.splitlines()
    return list

def find_common_item(string):
    mid = len(string)//2
    for char in string:
        if char in string[mid:]:
            return char

def calculate_priority(char):
    if ord(char) <= ord('Z'):
        priority = (ord(char) - ord('A')) + 27
    else:
        priority = (ord(char) - ord('a')) + 1
    return priority

#---------------------------------------------
#Part 2 Functions

def line_split(bigString):
    splitStrings = construct_list(bigString)
    bigList = []
    counter = 0
    temp = []
    for string in splitStrings:
        counter += 1
        temp.append(string)
        if counter == 3:
            bigList.append(temp)
            temp = []
            counter = 0
    return bigList

def find_common_letter(threeStrings):
    for char in threeStrings[0]:
        if char in threeStrings[1] and char in threeStrings[2]:
            return char

#------------------------------------------------

if __name__ == "__main__":
    with open("AdventofCode\\Day3\\input.txt") as f: #Reads in raw data
        input = f.read()

    bags = construct_list(input)
    sum1 = 0
    for bag in bags:
        sum1 += calculate_priority(find_common_item(bag))

    print(sum1) #Part 1 answer, sum of priorities of common items

    newGroups = line_split(input)
    sum2 = 0
    for group in newGroups:
        sum2 += calculate_priority(find_common_letter(group))

    print(sum2) #Part 2 answer, sum of priorities of group badges
