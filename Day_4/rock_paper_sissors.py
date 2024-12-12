import random
scissors = '''
    -------)
---'   -----------
       -----------)
       -----------)
---      (-----)
     '---(-----)
'''  
paper =  '''
    -------)
---'   -----------
       -----------)
       -----------)
---    -----------)
     '------------)
''' 
rock = '''
    ----------
---'   -------)
       (------)
       (------)
---    (------)
     '-(-----)
'''     
choice = int(input("what do you choose? Type 0 for rock, 1 for paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)
choice_list = [rock,paper,scissors]

if choice >= 3 or choice < 0:
     print("Please enter a valide numder to continue")
elif choice ==  computer_choice:
    print(f"{choice_list[choice]}\n computer chose:\n {choice_list[computer_choice]}\nWe have a draw")

elif choice == 0 and computer_choice == 2:
    print(f"{choice_list[choice]}\n computer chose:\n {choice_list[computer_choice]}\nYou win!")
elif choice == 1 and computer_choice == 0:
     print(f"{choice_list[choice]}\n computer chose:\n {choice_list[computer_choice]}\nYou win!")
elif choice == 2 and computer_choice == 1:
     print(f"{choice_list[choice]}\n computer chose:\n {choice_list[computer_choice]}\nYou win!")
else:
     print(f"{choice_list[choice]}\n computer chose:\n {choice_list[computer_choice]}\nYou lose")