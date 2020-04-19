
'''
TextBased Adventure Game

The Goal: Remember Adventure? Well, we’re going to build a more basic version of that.
A complete text game, the program will let users move through rooms based on user input and get descriptions of each room.
To create this, you’ll need to establish the directions in which the user can move, a way to track how far the user has moved (and therefore which room he/she is in), and to print out a description.
You’ll also need to set limits for how far the user can move.
In other words, create “walls” around the rooms that tell the user, “You can’t move further in this direction.”

Concepts to keep in mind:

Strings
Variables
Input/Output
If/Else Statements
Print
List
Integers


The tricky parts here will involve setting up the directions and keeping track of just how far the user has “walked” in the game.
I suggest sticking to just a few basic descriptions or rooms, perhaps 6 at most. This project also continues to build on using userinputted data.
It can be a relatively basic game, but if you want to build this into a vast, complex word, the coding will get substantially harder, especially if you want your user to start interacting with actual objects within the game.
That complexity could be great, if you’d like to make this into a longterm project. *Hint hint.
'''

# variables
path = 0

direction = str

# restart loop

while path != 3:


    # restart loop

    while path != 3:

        # game loop
        while path != 5:
            # start screen loop
            while path == 0:
                begin = str(input("Welcome to the new dungeon crawler adventure game! Type \"start\" to begin!\n"))

                if begin == "start":
                    print("As you walk through the dreary night a shady figure follows you home from work.")
                    path += 1
                else:
                    print("Invalid response!")

            print("You've had a long day and don't notice the tall dark shadow distancing himself from you.")

            direction = str(input("Suddenly you come to an intersection do you want to go left, right, or straight?"))

            # direction if statement 1
            if direction == "left":
                path = 10
                print("You chose to take the left path, still the shady character persists but he begins to speed up!")
            elif direction == "right":
                path = 15
                print("You chose to take the right path, the shady character begins to fall behind as you outpace him!")
            else:
                path = 20
                print("You finally notice the shady character and begin to pick up the pace going down the straight path.")

        # response if statement 1
            if path == 10:
                print("Once again you come to an intersection and finally you notice the character")
                direction = str(input("will you go left, right, or straight?"))
            elif path == 15:
                print("Once again you come to an intersection and finally you notice the character")
                direction = str(input("will you go left, right, or straight?"))
            else:
                print("As you continue running you come across another intersection,")
                direction = str(input("will you go left, right or straight?"))

        # direction if statement 2
            if direction == "left":
                path = 25
                print("You chose to take the left path, the tall, dark man is on your heels! you begin sprinting.")
            elif direction == "right":
                path = 30
                print("You chose to take the right path, the man is beginning to catch up!")
            else:
                path = 35
                print("You chose to go straight and continue running as fast as you can!")

        # response if statement 2
            if path == 25:
                print("The man unrelentingly hits you over the head with a club and knocks you out on site")
                path = 5
            elif path == 30:
                print("The man unrelentingly hits you over the head with a club and knocks you out on site")
                path = 5
            else:
                print("You look back after running 3 blocks at full speed and no longer see the strange man")
                path = 7
                break

        # Game over statement
        if path == 5:
            direction = str(input("\nGame over! The shady character murdered you! \nWould you like to try again? (y/n)"))
        else:
            direction = str(input("\nYou win! The shady character didn't catch you this time! \nWould you like to try again? (y/n)"))
        if direction == "y":
            path = 0
        else:
            path = 3

print("Thanks for playing!")

