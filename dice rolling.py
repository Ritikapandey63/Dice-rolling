"""
WAP that simulates simple dice rolling game.
1. Dice Roll : Random number form 1 to 6
2. User Input : The user should be abel to specify number of dice to roll.
3. Result Display : The program should display the resutl of each dice roll and the total sum.
"""
import random
while True:
    try:
        roll = int(input("Enter the number of rolldice : "))
        if roll > 0:
            break
        else:
            print("Enter Positive Value")

    except ValueError:
        print("Enter the integer value only")
   
L = [random.randint(1,6) for i in range(roll)]
sum = 0 
for val in L:
    sum = sum + val

print(L)
print("Total number : " , sum)