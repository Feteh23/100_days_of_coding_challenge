print(" Welcome to treasure island.\n Your mission is to find the treasure")
cross_raod = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if cross_raod == "left":
    lake = input('You came to a lake. There is an island in the middle of the land. Type "wait" to wait for a baot. Type "smim" to swim across\n')
    if lake == "wait":
        door = input("You arrive at the island unharmed. there is a house with 3 doore. one red, one yellow and one blue. which colour do you choose?\n")
        if door == "yellow":
            print("You found the treasure.You win")
        elif door == "blue":
            print("You enter a room of beast. Game over")
        else:
            print("You got attack by angry trout. Game over")
    else:
        print("Game over you drawn")
else:
    print("Game over you fell inside a hole")