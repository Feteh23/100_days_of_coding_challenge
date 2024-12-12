import random
name_string = input("Give me everybody's names, seperated by a comma.  ")
names = name_string.split(", ")
length = len(names) 
random_name = random.randint(0, length - 1)
name_to_pay = names[random_name]
print(f"{name_to_pay} is going to buy the meal today!")