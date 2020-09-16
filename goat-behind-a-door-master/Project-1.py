from random import randint

# Part 1 A Basic Game
print("------")
print("Part 1")
print("------")

car = randint(1, 3)

print("A car is behind 1 of 3 doors.")

guess = int(input("Which door would you like to pick? "))

print("You chose door #", guess, sep='', end='')
print(".")
print("The car was behind door #", car, sep='', end='')
print(".")

# Part 2 Reaving a Goat and Allowing the User to Switch
print("------")
print("Part 2")
print("------")

car = randint(1, 3)

print("A car is behind 1 of 3 doors.")
print("Behind the other 2 doors are goats.")

guess = int(input("Which door would you like to pick? "))

def main():
    global car
    global guess
    
    if guess == 1 and car == 1:
        print("There is a goat behind Door #2.")
        switch = input("Would you like to switch? ")
        change(switch)
    elif guess == 1 and car == 2:
        print("There is a goat behind Door #3.")
        switch = input("Would you like to switch? ")
        change(switch)
    elif guess == 1 and car == 3:
        print("There is a goat behind Door #2.")
        switch = input("Would you like to switch? ")
        change(switch)
    elif guess == 2 and car == 1:
        print("There is a goat behind Door #3.")
        switch = input("Would you like to switch? ")
        change(switch)
    elif guess == 2 and car == 2:
        print("There is a goat behind Door #3.")
        switch = input("Would you like to switch? ")
        change(switch)
    elif guess == 2 and car == 3:
        print("There is a goat behind Door #1.")
        switch = input("Would you like to switch? ")
        change(switch)
    elif guess == 3 and car == 1:
        print("There is a goat behind Door #2.")
        switch = input("Would you like to switch? ")
    elif guess == 3 and car == 2:
        print("There is a goat behind Door #1.")
        switch = input("Would you like to switch? ")
        change(switch)
    elif guess == 3 and car == 3:
        print("There is a goat behind Door #1.")
        switch = input("Would you like to switch? ")
        change(switch)

def change(switch):
    global guess
    global car
    
    if switch == "yes":
        guess = int(input("Which door would you like to switch to? "))
        if guess != car:
            result()
            print("You lost.")
        elif guess == car:
            result()
            print("You won!")
    else:
        if guess != car:
            result()
            print("You lost.")
        elif guess == car:
            result()
            print("You won!")

def result():
    print("The car was behind Door #", car, sep='', end='')
    print("!")
    print("You chose Door #", guess, sep='', end='')
    print(".")

main()
    
# Part 3 Building a Simulation
print("------")
print("Part 3")
print("------")

keep_going = "Y"

while keep_going == "Y":
    
    rounds = int(input("How many rounds of the game should be simulated? "))

    while rounds < 10 or rounds > 10000:
        print("You must enter a number between 10 and 10,000. ")
        rounds = int(input("Please try again: "))

    decision = input("Should the player switch or stay? ")

    while decision != "switch" and decision != "stay":
        print("Must enter either 'switch' or 'stay.'")
        decision = input("Please try again: ")

    if decision == "switch":
        
        wins = 0
        losses = 0
        
        for turn in range (1, rounds + 1):

            choice = randint(1, 3)
            car = randint(1, 3)

            if choice != car:
                wins += 0
            elif choice == car:
                wins += 1
        results = (wins / rounds)*100
        print("Player won", wins, end='')
        print("/", rounds, end='', sep='')
        print(" games.")
        print("That's", format(results, ",.2f"), end='')
        print("%!")

    elif decision == "stay":

        wins = 0
        losses = 0

        for turn in range (1, rounds + 1):

            choice = randint(1, 3)
            car = randint(1, 3)

            if choice != car:
                wins += 0
            elif choice == car:
                wins += 1

        results = (wins / rounds) * 100
        print("Player won", wins, end='')
        print("/", rounds, end='', sep='')
        print(" games.")
        print("That's", format(results, ",.2f"), end='')
        print("%!")

    keep_going = input("Would you like to start another round?  Enter 'Y' for yes: ")
