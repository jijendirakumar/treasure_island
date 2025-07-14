print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to Treasure IsLand.")
print("Your mission is to find a treasure..")

while True:
    choise_1 =input('You\'re at crossroad, where do you want to go ?'
                ' Type "left" or "right".\n').lower()
    if choise_1 == "left" :
        choise_2 = input('you\'ve come to lake.There is a Island in the middle of the lake.'
                'Type "wait" to wait for boat. Type "swim" to swim across.\n').lower()
        if choise_2 == "wait" :
            choise_3 = input('You\'ve arrived at Island Unharmmed.'
                         'There is house with three different colours of door .'
                         'one Red , one Yellow and one Blue .'
                         'Which colour do you choose ?\n').lower()
            if choise_3 == "Red" :
                print("Oh no! You walked into a room full of fire. Game Over!")
            elif choise_3 == "Yellow" :
                print("Congratulations! You found the treasure. You Win!")
            elif choise_3 == "Blue":
                print("Oh no! You entered a room full of beasts. Game Over!")
            else :
                print("Invalid choice. A trap door opens beneath you. Game Over!")
        else :
                print("You were attacked by a giant fish while swimming. Game Over!.....")
    else :
        print("You fell into a hole. Game Over!.......")
    retry = input("Do you want to play again? (yes/no): ").lower()
    if retry != "yes":
        print("Thanks for playing! Goodbye.")
        break

