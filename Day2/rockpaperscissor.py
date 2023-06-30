#Advent of Code - Day 2
#Sean O'Dea

#A - Rock 
#B - Paper
#C - Scissors

#X - Rock(1 point)
#Y - Paper(2 point)
#Z - Scissor(3 point)

#Loss - 0 points
#Draw - 3 points
#Win - 6 points

def construct_list(rawGuide):
    list = rawGuide.splitlines()
    for i in range(len(list)):
        list[i] = list[i].split()
    return list

def determine_win_points(elf, me):
    if elf == 'A' and me == 'X':
        #rock - rock -> Draw
        return 3
    elif elf == 'A' and me == 'Y':
        #rock - paper -> Win
        return 6
    elif elf == 'A' and me == 'Z':
        #rock - scissors -> Loss
        return 0
    elif elf == 'B' and me == 'X':
        #paper - rock -> Loss
        return 0
    elif elf == 'B' and me == 'Y':
        #paper - paper -> Draw
        return 3
    elif elf == 'B' and me == 'Z':
        #paper - scissors -> Win
        return 6
    elif elf == 'C' and me == 'X':
        #scissors - rock -> Win
        return 6
    elif elf == 'C' and me == 'Y':
        #scissors - paper -> Loss
        return 0 
    elif elf == 'C' and me == 'Z':
        #scissors - scissors -> Draw
        return 3
    else:
        print("Error")

def determine_move_points(move):
    if move == 'X':
        #Rock - 1 Point
        return 1
    elif move == 'Y':
        #Paper - 2 Points
        return 2
    elif move == 'Z':
        #Scissors - 3 Points
        return 3
    else:
        print("Error")

#---------------------------------------
#Part 2
# X - Loss
# Y - Draw
# Z - Win

def determine_move(elfMove, result):
    if result == 'X':
        #Loss
        if elfMove == 'A':
            #Rock
            return 'Z' #Scissors
        elif elfMove == 'B':
            #Paper
            return 'X' #Rock
        elif elfMove == 'C':
            #Scissor
            return 'Y' #Paper
        else:
            print("Error")

    elif result == 'Y':
        #Draw
        if elfMove == 'A':
            #Rock
            return 'X' #Rock
        elif elfMove == 'B':
            #Paper
            return 'Y' #Paper
        elif elfMove == 'C':
            #Scissor
            return 'Z' #Scissors
        else:
            print("Error")

    elif result == 'Z':
        #Win
        if elfMove == 'A':
            #Rock
            return 'Y' #Paper
        elif elfMove == 'B':
            #Paper
            return 'Z' #Scissors
        elif elfMove == 'C':
            #Scissor
            return 'X' #Rock
        else:
            print("Error")
    else:
        print("Error")


if __name__ == "__main__":
    with open("AdventofCode\\Day2\\input.txt") as f: #Reads in raw data
        input = f.read()
    guide = construct_list(input)

    part1Sum = 0
    for game in guide:
        part1Sum += determine_win_points(game[0], game[1]) 
        part1Sum += determine_move_points(game[1])

    print(part1Sum) #Part 1 answer, sum of user points

    part2Sum = 0
    for game in guide:
        #determines new move to calculate new point amount
        part2Sum += determine_win_points(game[0], determine_move(game[0], game[1])) 
        part2Sum += determine_move_points(determine_move(game[0], game[1]))
    print(part2Sum) #Part 2 answer, sum of user points with altered logic