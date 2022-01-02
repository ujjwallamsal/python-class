import random 
min_val = 1
max_val = 50
roll_again = "yes"
while roll_again == "yes" or roll_again == "y":  
    print("Rolling The Dices...")
    print("The Values are :")
    r1 = random.randint(min_val, max_val)
    r2 = random.randint(min_val, max_val)
    print(r1)
    print(r2)
    roll_again = input("Roll the dices again? (yes/no) : ") 
    if roll_again == "no" or roll_again == "n":
        print("Thanks for playing!")
        break