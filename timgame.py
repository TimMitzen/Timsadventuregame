#tims adventure game
#start area, can go left, right, up, down
#up in montser room
#down is hallway - contuines to next area
#left is trap - 3 options 1 is to hallway 2 is to treasure room 3 die and game over
#right treasure room pick treasure gold - gives gold to player - extra life gives extra life to player if they die
from sys import exit
player_inventory =[]
player_life = []
#start function print name of game and the starting point
def start():
    print("This is Tim adventure game!")
    print("Type start to play, or q for quit.")

    start = input('> ')
    #if type start go starting starting room
    #if type quit quit game or else put in the correct commands
    action_start_commands = ["start", "s", "q", "quit"]
    while start.lower() not in action_start_commands:
        print("Try again")
        start = input("> ")
    if start.lower() == 'start':
        starting_room()
    elif start.lower() == 'q' or start.lower() == 'quit':
        exit("Game over")
    else:
        print("Try again.")



#give the availiable actions left, right, up, down

#left = trap fuction if 3 die , if 2 treasure room 1 hallway
def trap():
    #trap commends 1 , 2 ,3
    #if trap commands == 1 go to the hallway fuction
    #elif if trap commends == 2 go to treasure room fuction
    #elif if trap commends == 3 you die command
    print("You have enter a trap.")
    print("You have 3 options")
    print("1. Try to break it.")
    print("2. Try to disarm it.")
    print("3. Try to slip out of it")
    #this is for the user
    action_command = input("> ")
    #for acceptable commennds
    trap_commands = ['1', '2', '3']
    #if this happens print below needs to be not in
    while action_command not in trap_commands:
        print("Enter a valid command")

        action_command = input("> ")
    #if 1 go to hallway function
    if action_command == '1':
        hallway()
    #if 2 go to treasure function
    elif action_command == '2':
        treasure_room()
    #if 3 go to die commend
    elif action_command == '3':
        die()
    else:
        print("Try again.")


def hallway():
    print("You are in the hallway.")
    #this is the commands the function will only take
    hallway_commands = ["left", "right", "l", "r"]
    print("You can go left or right.")
    #user input
    hallway_command = input("> ")
    #for wrong user input
    while hallway_command not in hallway_commands:
        print("Enter a correct command")
        hallway_command = input("> ")
    #if the user picks left
    if hallway_command.lower() == "left" or hallway_command.lower() == "l":
        trap()
    #if user picks right
    elif hallway_command.lower() == "right" or hallway_command.lower() == "r":
        after_hallway()
    else:
        print("Try again.")
def die():
    #ask if player want to play again if not exit if they do begin again
    player_lifes = sum(player_life)
    if player_lifes == 0:
        print("Game over! Do you want to play again y/n?")
        die_command = input("> ")


        if die_command.lower() == 'y':
            start()
        elif die_command.lower() == 'n':
            exit(0)
        else:
            print("Enter a valid commend.")
    elif player_lifes == 1:
        print("You are magically back in the hallway!!")
        player_life.clear()
        hallway()


def treasure_room():
    print("This is the treasure room.")

    print("You can pick a treasure.")
    print("Hit 1 for door one.")
    print("Hit 2 for door two.")
    treasure_commands = ["1", "2"]
    treasure_command = input("> ")
    #this is for the command is typed in wrong
    while treasure_command not in treasure_commands:
        print("Enter a valid command.")
        treasure_command = input("> ")
        #if treasure command is 1 do below
    if treasure_command.lower() == "1":
        gold = 100
        player_inventory.append(gold)
        print(f"You have {gold} gold now.")
        hallway()
        #if the command is 2
    elif treasure_command.lower() == "2":
        life = 1
        #appends to the player_life list
        player_life.append(life)
        print("You have an extra life.")
        hallway()
    else:
        print("Try again.")

def monster_room():
    print("This is the montser room.")
    print("Monster comes after you, What do you do?")
    #assign 100 to player and monster health
    monster_health = 100
    player_health = 100
    print("1. Punch monster.")
    print("2. Drop kick the monster.")
    player_action = input('> ')
    #if player picks 1 do the math below then go to the hallway
    if player_action == '1':
        monster_health =  monster_health - 100
        print(f"You killed the monster{monster_health}")
        hallway()
    elif player_action == "2":
        #if this happens player and monsters goes to half health
        monster_health = monster_health - 50
        player_health = player_health - 50
        ## TODO: make this a function and call it
        #if player heath and montser health is 50 do bellow make this a function and call it here
        if player_health == 50 and monster_health == 50:

            print(f"Monster is still alive!, Your health is down to {player_health}")
            print("What do you want to do?")
            print("1. Flee for your life.")
            print("2. Scream at it.")
            print("3. Give up.")
            player_action = input('> ')
            #if player action is 1 go to hallway function

            if player_action == '1':
                hallway()
            #if this is 2 do the math and go to the hallway
            elif player_action == '2':
                monster_health = monster_health - 50
                print(f"You hit the monster with your special power and the monsters health is {monster_health}")
                print("The monster is dead")
                treasure_room()
            #if 3 do the math and go die function
            elif player_action == "3":
                player_health = player_health - 50
                print("The monster hits you with his uglyness.")
                print(f"You health is {player_health}, you died.")
                die()
            else:
                print("Try again")

        else:
            print("Try again.")

    else:
        print("Try again")





#right -trap function left- treasrue room function , up monstor room function down hallway function
def starting_room():
    print("This is the starting room")
    print("You can go left, right, down and up. Type l for left. You can type r for right, type u for up, type d for down.")
    action_room_commands = ["right", "r","left","l","up","u", "down", "d"]
    starting_commands = input("> ")
    while starting_commands not in action_room_commands:
        print("Please enter a correct command")
        starting_commands = input("> ")
    if starting_commands.lower() == "right" or starting_commands.lower() == 'r':
        trap()
    elif starting_commands.lower() == "left" or starting_commands.lower() == "l":
        treasure_room()
    elif starting_commands.lower() == "up" or starting_commands.lower() == "u":
        monster_room()
    elif starting_commands.lower() == "down" or starting_commands.lower() == "d":
        hallway()
    else:
        print("Try again")


def after_hallway():
    print("You have reached the second room after the hallway.")
    print("You can go left, right or down. R for right, L for left and D for down.")
    after_hallway_commands = ["left", "l", "right", "down", "d","r"]
    after_hallway_command = input("> ")
    #this where error message comes up if wrong thing is typed
    while after_hallway_command not in after_hallway_commands:
        print("Enter valid command.")
        after_hallway_command = input("> ")
        #for movement of player
    if after_hallway_command.lower() == 'left' or after_hallway_command.lower() == 'l':
        treasure_room()
    elif after_hallway_command.lower() == "right" or after_hallway_command.lower() == "r":
        trap()
    elif after_hallway_command.lower() == "down" or after_hallway_command.lower() == "d":
        finish_room()

def finish_room():
    print("You are won the game!!!")
    print("Great Job")


start()
