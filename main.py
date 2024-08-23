# 1 2 1
# 1 3 3
# 2 1 1
# 2 3 2
# 3 1 3
# 3 2 2

import random
selection_list = ["Snake", "Water", "Gun"]

print("Select Your Choice from the list below and enter curresponding number")
print("1 Snake")
print("2 Water")
print("3 Gun")
print("0 to Exit the Game")
while True:
    int_user_selection = int(input("Enter Your Selection : "))
    int_alexa_selection = random.randint(1, 3)
    if(int_user_selection == 0):
        break
    else:
        print(f"You Choose {selection_list[int_user_selection - 1]}")
        print(f"I Choose {selection_list[int_alexa_selection - 1]}")
        if(int_alexa_selection == int_user_selection):
            print("\nIt's a Draw!!")
        elif(int_alexa_selection == 1 and int_user_selection == 2):
            print("\nYou are lose!")
        elif(int_alexa_selection == 2 and int_user_selection == 3):
            print("\nYou are lose!")
        elif(int_alexa_selection == 3 and int_user_selection == 1):
            print("\nYou are lose!")
        elif(int_alexa_selection == 1 and int_user_selection == 3):
            print("\nYou Win Congratulations!")
        elif(int_alexa_selection == 2 and int_user_selection == 1):
            print("\nYou Win Congratulations!")
        elif(int_alexa_selection == 3 and int_user_selection == 2):
            print("\nYou Win Congratulations!")
        else:
            print("\nSomething went Wrong!")
            print("Sorry!")
            break
print("You Quit the Game")