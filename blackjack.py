# This is the starter code for the Fundementals of Programming w/ Python course
# You may work direclty from this file or create a copy of it.
#
# It is a good idea to start by coding each function and then
# coding the game play in the main line of the program
#
# You may of course add your own variables and functions
#
# NOTE: *DO NOT USE THE GLOBAL KEYWORD*

import random

# VARIABLES

deck = []
player_hand = []
dealer_hand = []
rounds_played = 0


# FUNCTIONS

def create_deck(deck):
    """
    Creates and returns a deck of 52 cards. The cards are in the form 102,206,412 etc. 

    :return: List of ints

    EXAMPLE:
    deck = create_deck(deck)
    print(deck)

    >>> [101,102,103,104,105,106,107,108,109,110,111,112,113,201,202,203,204,205,206,207,208,209,210,211,212,213,301,302,303,304,305,306,307,308,309,310,311,312,313,401,402,403,404,405,406,407,408,409,410,411,412,413]
    """
    #suits = [100,200,300,400]
    deck = []
    max_rank = 13
    suit = 100
    max_suit = 400
    
    #while + for loop solution
    while suit <= max_suit:
        for j in range(max_rank):
            deck.append(suit+j+1)
        suit += 100
    return deck
    
    #2 x for loop solution
    # for i in range(len(suits)):
    #     for j in range(max_rank):
    #         deck.append(suits[i]+j+1)
    
    pass

def shuffle_deck(deck):
    """
    Shuffles the deck of cards passed in the paramater deck.

    :param deck: a list of cards
    :return: None

    EXAMPLE:
    deck = create_deck(deck)
    shuffle_deck(deck)
    print(deck)
    
    >>> [201, 302, 410, 210, 213, 108, 309, 101, 408, 206, 404, 107, 205, 308, 110, 402, 306, 407, 212, 311, 304, 111, 109, 303, 102, 310, 207, 312, 103, 411, 305, 208, 105, 313, 403, 413, 202, 112, 409, 106, 104, 113, 211, 307, 401, 204, 412, 203, 301, 209, 405, 406]
    """
    random.shuffle(deck)
    return deck
    pass

def deal_cards(deck, n):
    """
    Deals n cards from the given deck. The cards dealt
    will be removed from the deck passed and returned from
    the function in a list.

    :param deck: list of cards
    :param n: int
    :return: list of cards

    EXAMPLE:
    deck = create_deck(deck)
    shuffle_deck(deck)
    cards = deal_cards(deck, 4)
    print(cards)
    print(len(deck))

    >>> [101,205,313,306]
    >>> 48
    """
    cards = []
    cards = deck[:n] #get first n cards from deck
    del deck[:n] #delete first n cards from deck
    return cards
    return deck
    
    

def hand_value(hand):
    """
    Calculates and returns the value of the given hand.
    Always returns the BEST possible value (be careful with aces).
    
    :param hand: list of cards
    :return: int

    EXAMPLES:
    player_hand = [101,211]
    value = hand_value(player_hand)
    print(value)
    >>> 21

    player_hand = [113,211]
    value = hand_value(player_hand)
    print(value)
    >>> 20

    player_hand = [113,211, 107]
    value = hand_value(player_hand)
    print(value)
    >>> 27

    player_hand = [205,305, 407,201]
    value = hand_value(player_hand)
    print(value)
    >>> 18
    """
    ace = False
    value = 0
    
    for card in hand:
        rank = card % 100
        if rank == 1:
            value += 1
            ace = True
        elif rank >= 10:
            value += 10
        else:
            value += rank
    
    if value > 21 and ace:
        value -= 10
        
    return value
    
    pass


def is_over(hand):
    """
    Returns a boolean value representing if a given
    has busted or is over 21.

    :param hand: list of cards
    :return: bool

    EXAMPLE:
    hand = [110,210,310]
    print(is_over(hand))
    >>> True

    hand = [101,210,310]
    print(is_over(hand))
    >>> False

    hand = [105, 207]
    print(is_over(hand))
    >>> False
    """
    
    busted = False
    
    if hand_value(hand) > 21:
        busted = True
    
    return busted
        
    pass

def compare_hands(hand1, hand2):
    """
    Comapres two hands to see if hand1 is better than hand2.
    If hand1 is better than the function returns 1, if the hands
    are the same returns 0. Otherwise if hand2 is better than 1 returns -1.

    :param hand1: list of cards
    :param hand2: list of cards
    :return: int

    EXAMPLES:
    player_hand = [101,110]
    dealer_hand = [210,311]
    print(compare_hands(player_hand, dealer_hand))
    >>> 1
    
    player_hand = [101,110]
    dealer_hand = [210,311]
    print(compare_hands(dealer_hand, player_hand))
    >>> -1

    player_hand = [101,110]
    print(compare_hands(player_hand, player_hand))
    >>> 0

    """
    hand1_val = hand_value(hand1)
    hand2_val = hand_value(hand2)
    
    if hand1_val > hand2_val and not(is_over(hand1)):
        return 1
    elif hand1_val < hand2_val and not(is_over(hand2)):
        return -1
    elif hand1_val == hand2_val:
        return 0
    
    pass

def get_hit_or_stay():
    """
    Gets a decision of whether to hit or stay from the user.
    Returns True if the user hits and False if the user stays. The
    function should keep asking for input until it recives "hit" or "stay".
    The case in which the user types "hit" or "stay" should not matter. For 
    example, "STay" should work to stay.

    :return: Bool

    EXAMPLES:
    decision = get_hit_or_stay()
    >>> Would you like to hit or stay? no
    >>> Not a valid option, try again.
    >>> Would you like to hit ot stay? HiT
    print(decision)
    >>> True

    decision = get_hit_or_stay()
    >>> Would you like to hit or stay? stay
    print(decision)
    >>> False
    """
    
    choice = input("Would you like to hit or stay?: ").lower()
    
    valid = False
    
    while valid == False:
        if choice == "hit":
            valid = True
            return True
        elif choice == "stay":
            valid = True
            return False
        else:
            valid = False
            print("Not a valid option try again.")
            choice = input("Would you like to hit or stay?: ").lower()
    pass

# MAINLINE
# This is where you will implement the code to play the game

welcome = """
Welcome to Blackjack!
---------------------
"""

print(welcome)

play = "go"

while play == "go":
    deck = create_deck(deck)
    print("Round ",str(rounds_played+1)," has started")
    shuffle_deck(deck)
    initial_cards = deal_cards(deck, 4)
    player_hand = initial_cards[:2]
    dealer_hand = initial_cards[2:]
    print("The cards have been dealt")
    player_hand_string = ' , '.join(str(i) for i in player_hand)
    print("Your cards: ",player_hand_string)
    print("Dealer cards: ",str(dealer_hand[0]),", hidden")
    decision = get_hit_or_stay()
    stay_resp = "You decided to stay, your turn is over. The dealer's turn has started."
    reveal_hidden = "The dealer reveals their hidden card is a"
    hit_resp = "You hit and received the card: "
    player_stay = False
    dealer_stay = False
    player_bust = False
    dealer_bust = False
    while decision == True:
        player_hit = deal_cards(deck,1)
        print(hit_resp,str(player_hit[0]))
        player_hand.append(player_hit[0])
        player_hand_string = ' , '.join(str(i) for i in player_hand)
        print("Your cards",player_hand_string)
        player_bust = is_over(player_hand)
        if player_bust is True:
            print("You BUST and have lost this round.")
            player_bust = True
            cont = input("Would you like to play again? [Y/N]").lower()
            if cont == "y" or cont[0] == "y":
                play = "go"
                rounds_played += 1
                print("------------------")
            elif cont == "n" or cont[0] == "n":
                play = "no"
            break
        else:
            decision = get_hit_or_stay()
            if decision is False:
                player_stay = True
    
    if decision == False:
        print(stay_resp)
        if player_bust == False:
            print(reveal_hidden,dealer_hand[1])
            print("Dealers Cards: ",str(dealer_hand[0]),",",str(dealer_hand[1]))
        else:
            continue
        dealer_value = hand_value(dealer_hand)
        while dealer_value < 17:
            dealer_hit = deal_cards(deck,1)
            print("Dealer hits and received: ",str(dealer_hit[0]))
            dealer_hand.append(dealer_hit[0])
            dealer_value = hand_value(dealer_hand)
            if is_over(dealer_hand) is True:
                print("The Dealer is BUST and have lost round.")
                dealer_bust= True
                cont = input("Would you like to play again? [Y/N]").lower()
                if cont == "y" or cont[0] == "y":
                    play = "go"
                    rounds_played += 1
                    print("------------------")
                elif cont == "n" or cont[0] == "n":
                    play = "no"
                break
            elif dealer_value >= 17:
                print("Dealer stays")
                dealer_stay = True
                break
            else:
                continue
        dealer_stay = True
    
    if player_stay and dealer_stay == True and dealer_bust == False:
        print("Dealer has ",str(hand_value(dealer_hand)))
        print("You have ",str(hand_value(player_hand)))
        result = compare_hands(dealer_hand, player_hand)
        if result == 1:
            print("Dealer wins")
        elif result == -1:
            print("You win")
        elif result == 0:
            print("Draw")
        cont = input("Would you like to play again? [Y/N]").lower()
        if cont == "y" or cont[0] == "y":
            play = "go"
            rounds_played += 1
            print("------------------")
        elif cont == "n" or cont[0] == "n":
            play = "no"