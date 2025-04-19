import random # imports random library
cards  = ["Diamonds", "Spades", "Hearts", "Clubs"] # variable holding the 4 card suits
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"] # variable thats holding all 13 card numbers/types

def pick_a_card(): # subroutine that picks the card and returns it to the terminal
        card = random.choices(cards)
        rank = random.choices(ranks)
        return (f"The {rank} of {card}") # string handling used to implement both 'cards' and 'ranks' variables into the output

print(pick_a_card()) # prints the output to the screen
