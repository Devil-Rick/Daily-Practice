print('Welcome to Treasure Island.')
print('Your mission is to find the treasure.')

direction = input(
    "You're at the crossroad. Where do you want to go? Type \"Left\" or \"Right\" \n")
if direction.lower() == 'left':
    activity = input(
        'You come to a lake. There is an island in the middle of the lake.Type wait to \"wait\" for a boat. Type \"swim\" to swim across. \n')
    if activity.lower() == 'wait':
        room = input(
            'You arrived at the island unharmed. There is a house with 3 doors . One \"Red\" one \"Blue\" one \"Yellow\" \n Choose wisely. \n')
        if room.lower() == 'red':
            print('Congrats you have found the Treasure')
            print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

        elif room.lower() == 'blue':
            print(
                'You have entered in a room of Beasts.....\nGame Over !!!! Sorry wrong Choice ')
        else:
            print(
                "You have entered in a room of deadly insects.....\nGame Over !!!! Sorry wrong Choice")
    else:
        print('You got eaten by sharks. Worst way to die I guess .... \nGame Over !!!! Sorry wrong Choice')
else:
    print('You have choosen the wrong direction although its Right ... \n Game Over !!!! Sorry wrong Choice')
