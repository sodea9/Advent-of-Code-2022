#Advent of Code - Day 1
#Sean O'Dea

import string

def construct_list(numbers):
    calorie_list = []
    groups = numbers.split('\n\n')
    for group in groups:
        calorie_list.append(group.splitlines())
    return calorie_list

def string_to_int(stringList):
    intList = list(map(int, stringList))
    return intList


if __name__ == '__main__':
    with open("AdventofCode\Day1\\input.txt") as f: #Reads in raw data
        input = f.read()

    lis = (construct_list(input)) #Processes into malleable list

    for i in range(len(lis)):
        lis[i] = string_to_int(lis[i]) #Converts list of strings into integers

    sums = []
    for elf in lis:
        sums.append(sum(elf))
    print((max(sums))) #Part 1 Answer Biggest sum
    print()

    top3 = []
    for i in range(3): #Part 2, finds top 3 most calories
        print((max(sums)))
        top3.append((max(sums)))
        sums.remove(max(sums))
    
    print(sum(top3)) #Part 2 Answer, sum of top 3
