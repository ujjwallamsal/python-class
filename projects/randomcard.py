import random
cards = ["Diamonds", "Spades", "Hearts", "Clubs"]
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
def pick_a_card():
    card = random.choices(cards)
    rank = random.choices(ranks)
    # res = "The {} of {}".format(rank, card)
    res = f"The {rank} of {card}"
    return res
roll_again = "yes"
while roll_again == "yes" or roll_again == "y":
    result = pick_a_card()
    print(result)
    roll_again = input("Pick again? (yes/no) ")
    if roll_again == "no" or roll_again == "n":
        print("Thanks for playing!")
        break