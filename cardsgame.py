from random import shuffle


SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """


    def __init__(self):


    def shuffling(self):
        num = shuffle(self.RANKS)
        typ = shuffle(self.SUITE)
        return num, typ
    pass


#Game starting
print("Welcome to War, let's begin...")
newGame = Deck()
print (newGame.RANKS)
#player_name = input("Please enter your player name:")
