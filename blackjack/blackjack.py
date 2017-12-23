# Going to try out making a blackjack game
# Let's see how feature rich it can become

from sys import exit
import time
import random

# *******************************************************

def bj_deck(num):
    """Creates the full deck based on the number of decks the player wants to use"""
    if num < 1 or num > 6:
        print("Idiot, can you read?")
        exit(0)
    cards = [ 'ad', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'jd', 'qd', 'kd',
    'ac', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'jc', 'qc', 'kc',
    'ah', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'jh', 'qh', 'kh',
    'as', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'js', 'qs', 'ks' ]
    return cards * num

# *******************************************************

def shuffle(deck):
    """Shuffles deck, a deck of cards must be passed"""
    passes = 0
    if len(deck)%52 != 0:
    # Make sure you have a full deck
        exit(1)

    while passes < 5:
    # Thoroughly shuffle the cards
        for card in range(0,len(deck),random.randint(1,3)):
            rcard = deck.pop(card)
            deck.insert(random.randint(0,len(deck)), rcard)
        passes += 1   
 
    if len(deck) > 104:
    # Insert a shoe if you have more 3 decks or more
        shoePosition=random.randint(48, 76)
        deck.insert(-shoePosition, "shoe")
    #print deck
    return deck

# *******************************************************

def deal(deck):
    """This funtion deals the cards"""
    # define local variables
    shoe = False
    yourHand = []
    dealerHand = []
    for i in range(0,2):
    # Deal the dealer and player(s)
        if deck[0] == shoe:
            shoe = True
            print("We've hit the cut")
            deck.pop(0)
            yourHand.append(deck.pop(0))    
            count(yourHand[-1],runningCount)
        else:
            yourHand.append(deck.pop(0))
            dealerHand.append(deck.pop(0))
            count(yourHand[-1],runningCount)
        if len(dealerHand) == 2:
		count(dealerHand[-1],runningCount)
    
    #print deck
    #print("Your Hand: {}".format(yourHand))
    #print("Dealer Hand: {}, {}".format('xx',dealerHand[1]))
    return {"yourHand":yourHand, "dealerHand":dealerHand, "shoe":shoe } 

# *******************************************************

def count(card, count):
    """Tallies the running count of the cards in case you want to practice"""
    if '2' in card:
        count += 1
    elif '3' in card:
        count += 1
    elif '4' in card:
        count += 1
    elif '5' in card:
        count += 1
    elif '6' in card:
        count += 1
    elif '10' in card:
        count -= 1
    elif 'a' in card:
        count -= 1
    elif 'j' in card:
        count -= 1
    elif 'q' in card:
        count -= 1
    elif 'k' in card:
        count -= 1
    else:
        return count 
    return count

# *******************************************************

def handValue(hand):
    """Value passed must be a list representing a hand, return value will be an integer"""
    handValue = 0
    aceCount = 0

    for card in hand:
    # do the count 
        if '2' in card:
            handValue += 2 
        elif '3' in card:
            handValue += 3
        elif '4' in card:
            handValue += 4
        elif '5' in card:
            handValue += 5
        elif '6' in card:
            handValue += 6
        elif '7' in card:
            handValue += 7
        elif '8' in card:
            handValue += 8
        elif '9' in card:
            handValue += 9
        elif '10' in card:
            handValue += 10
        elif 'j' in card:
            handValue += 10
        elif 'q' in card:
            handValue += 10
        elif 'k' in card:
            handValue += 10
        elif 'a' in card:
            handValue += 1
            aceCount += 1
    
    if aceCount > 0 and handValue <= 11:
    # check if the hand has any aces that can be counted as "hard" aces and add 10
        handValue += 10
    return handValue


# *******************************************************

def shoeCheck(deck):
    """Function must receive a deck and will check for the presence of a cut card or shoe """
    if deck[0] == 'shoe':
        deck.pop(0)
        return True
    else:
        return False


# *******************************************************

def clearHand(hand):
   """This clears a hand of all cards"""
   for card in hand:
      hand.pop(0)
      return hand

# *******************************************************

def dealTheDealer(hand,deck):
    """Function to deal the dealer their cards"""
    while True:
    # This function assumes that the dealer stays on soft 17
        if handValue(hand) < 17:
            shoeCheck(deck)
            hand.append(deck.pop(0))
            print("Dealer hand: {}".format(hand))
            time.sleep(2)
        else:
            print("Dealer hand: {}".format(hand))
            return hand
            break

# *******************************************************

def playerAction(action, playerHand, dealerHand, deck):
    """ This function is called each time the action is on the player """
    shoe = shoeCheck(deck)
    if 'hit' in action or 'double' in action or '1' in action or '2' in action:
    # if the player chose to hit or double, this is what gets executed
        shoeCheck(deck)
        playerHand.append(deck.pop(0))
        print "decided to hit"
        return playerHand
    elif 'split' in action or '4' in action:
        playerHand1 = []
        playerHand2 = [] 
        #playerHand1.append(playerHand.pop(0))
        #playerHand2.append(playerHand.pop(0))
        playerHand1.append(playerHand.pop(0))
        playerHand2.append(playerHand.pop(0))
        shoeCheck(deck)
        playerHand1.append(deck.pop(0))
        shoeCheck(deck)
        playerHand2.append(deck.pop(0))
        return playerHand1, playerHand2
    elif 'stay' in action or '3' in action:
    # if the player chose to stay, this is what gets executed
        print "you decided to stay"
        return playerHand
    else:
        print "Unknown action, try again"
        return 1

# *******************************************************

def hit(deck, playerHand):
    """This function is called when the player choses to hit"""
    shoeCheck(deck)
    playerHand.append(deck.pop(0))
    print("You decided to hit")
    return playerHand

# *******************************************************

def stay(hand):
    """This function is called when a player decided to stay"""
    print("You decided to stay")
    print("Your Hand: {}".format(hand))

# *******************************************************

def split(deck, hand, dealerHand):
    """This function is called when a player chooses to split """
    split = 1
    hand1 = []
    hand2 = []
    hand1.append(hand.pop(0)) 
    hand2.append(hand.pop(0))
    dHands = {'1':hand1, '2':hand2} 
    action = ''
    clearSplit = 0
    print("You decided to split")
    for hands in dHands:
    # this loops through each hand after a split, only one initial split allowed
        while handValue(dHands[hands]) < 21:
            if len(dHands[hands]) < 2:
                dHands[hands].append(deck.pop(0))
            printHand(dHands[hands], dealerHand, split)
            action = raw_input('> ')
            if 'hit' in action or '1' in action:
                print("You decided to hit")
                hit(deck, dHands[hands])
            elif 'double' in action or '3' in action:
                print("You decided to double, good luck")
                hand = hit(deck, dHands[hands])
                print ("Your hand: {}".format(dHands[hands]))
                split += 1
                break
            elif 'stay' in action or '2' in action:
                print("You decided to stay")
                split += 1
                break

    dealTheDealer(dealerHand, deck)
    print("First Hand:")
    handOutcome(dHands['1'], dealerHand, clearSplit)
    clearSplit += 1
    print("Second hand:")
    handOutcome(dHands['2'], dealerHand, clearSplit)

# *******************************************************

def handOutcome(hand, dealerHand, clearSplit):
    """This function displays to the user whatever the outcome of a hand was"""
   
    handQuant = handValue(hand)
    dealerQuant = handValue(dealerHand)

    if clearSplit == 0:
        if dealerQuant == 21 and len(dealerHand) == 2:
            print("Dealer has Black Jack!!!") 
            print("You have: {}".format(handQuant))
            print("Dealer has: {}".format(dealerQuant))
            clearHand(hand)

        elif handQuant == 21 and len(hand) == 2:
            print("You have BlackJack!!")
            print("You have: {}".format(handQuant))
            print("Dealer has: {}".format(dealerQuant))
            clearHand(hand)

        elif handQuant > 21:
            print("You have: {}".format(handQuant))
            print("Dealer has: {}".format(dealerQuant))
            print("You broke!\n")
            clearHand(hand)
 
        elif dealerQuant > 21:
            print("You have: {}".format(handQuant))
            print("Dealer has: {}".format(dealerQuant))
            print("Dealer broke, you win!!!!\n")
            clearHand(hand)

        elif handQuant > dealerQuant:
            print("You have: {}".format(handQuant))
            print("Dealer has: {}".format(dealerQuant))
            print("You win!!\n")
            clearHand(hand)

        elif handQuant < dealerQuant:
            print("You have: {}".format(handQuant))
            print("Dealer has: {}".format(dealerQuant))
            print("Dealer Wins!!\n")
            clearHand(hand)

        elif handQuant == dealerQuant:
            print("You have: {}".format(handQuant))
            print("Dealer has: {}".format(dealerQuant))
            print("Push")
            clearHand(hand)

    if clearSplit == 1:
        if dealerQuant == 21 and len(dealerHand) == 2:
            print("Dealer has Black Jack!!!") 
            print("You have: {}".format(handQuant))
            print("Dealer has: {}".format(dealerQuant))
            clearHand(hand)
            clearHand(dealerHand)
        elif handQuant == 21 and len(hand) == 2:
            print("You have BlackJack!!")
            print("You have: {}".format(handQuant))
            print("Dealer has: {}".format(dealerQuant))
            clearHand(hand)
            clearHand(dealerHand)
        elif handQuant > 21:
            print("You have: {}".format(handQuant))
            print("Dealer has: {}".format(dealerQuant))
            print("You broke!\n")
            clearHand(hand)
            clearHand(dealerHand)
 
        elif dealerQuant > 21:
            print("You have: {}".format(handQuant))
            print("Dealer has: {}".format(dealerQuant))
            print("Dealer broke, you win!!!!\n")
            clearHand(hand)
            clearHand(dealerHand)

        elif handQuant > dealerQuant:
            print("You have: {}".format(handQuant))
            print("Dealer has: {}".format(dealerQuant))
            print("You win!!\n")
            clearHand(hand)
            clearHand(dealerHand)

        elif handQuant < dealerQuant:
            print("You have: {}".format(handQuant))
            print("Dealer has: {}".format(dealerQuant))
            print("Dealer Wins!!\n")
            clearHand(hand)
            clearHand(dealerHand)

        elif handQuant == dealerQuant:
            print("You have: {}".format(handQuant))
            print("Dealer has: {}".format(dealerQuant))
            print("Push")
            clearHand(hand)
            clearHand(dealerHand)

# *******************************************************

def bjCheck(hand):
    """This function checks if a hand has blackjack"""
    if len(hand) == 2 and handValue(hand) == 21:
    # function will return 0 if the hand is a blackjack
        return 0
    else:
    # function will otherwise return a 1
        return 1

# *******************************************************

def printHand(hand, dealerHand, splitNumber):
    """This function is called to print what the player and dealer have"""
    if splitNumber == 0:
        print("")
    if splitNumber == 1:
        print("Your first hand: {}".format(hand))
        print("Dealer hand: {}, {}".format('xx', dealerHand[1]))
        print("You have: {} \n 1. hit \n 2. stay \n 3. double".format(handValue(hand)))
    elif splitNumber == 2:
        print("Your second hand: {}".format(hand))
        print("Dealer hand: {}, {}".format('xx', dealerHand[1]))
        print("You have: {} \n 1. hit \n 2. stay \n 3. double".format(handValue(hand)))
    else:       
        print("Your hand: {}".format(hand))
        print("Dealer hand: {}, {}".format('xx', dealerHand[1]))
        print("You have: {} \n 1. hit \n 2. stay \n 3. double".format(handValue(hand)))

# *******************************************************

def playGame(deck):
    """Main function used to play the game"""
    runningCount = 0
    shoe = False
    shoepass = False
    yourHand = []
    yourHand1 = []
    yourHand2 = []
    dealerHand = []
    d = {}
    brokenHand = []
    playerActionDict = {}
    dSplit = {}    

    while True:
    # Outer while loop is used to go through a shoe
        d = deal(deck) 
        yourHand = d["yourHand"] 
        dealerHand = d["dealerHand"]
        shoe = d["shoe"]
        action = ''
        while True:
        # This inner loop goes through an entire hand    
            splitAction = 0
            if len(dealerHand) == 2 and not bjCheck(dealerHand):
            # Check if the dealer has blackjack and start a new hand if they do
                break
            else:
                if yourHand[0][:-1] == yourHand[1][:-1] and len(yourHand) == 2:
                # Check if the player can split their hand and give them the option 
                    print("Your Hand: {}".format(yourHand))
                    print("Dealer Hand: [{}, {}]".format('xx', dealerHand[1]))
                    if len(yourHand) == 2:
                        print ("You have {}: \n 1. hit \n 2. stay \n 3. double \n 4. split".format(handValue(yourHand))) 
                    else:
                        print ("You have {}: \n 1. hit \n 2. stay".format(handValue(yourHand))) 
  
                    action = raw_input('> ')
                    if 'stay' in action or '2' in action:
                        stay(yourHand)
                        break
                    #playerAction(action, yourHand, dealerHand, deck)
                    if 'double' in action or '3' in action:
                        # playerAction(action, yourHand, dealerHand, deck)
                        hit(deck, yourHand)
                        break
                    if 'hit' in action or '1' in action:
                        hit(deck, yourHand)
                    if 'split' in action or '4' in action:
                        splitAction = 1
                        split(deck, yourHand, dealerHand)
                        break

                else:
                    print("Your Hand: {}".format(yourHand))
                    print("Dealer Hand: {}, {}".format('xx',dealerHand[1]))
                    if handValue(yourHand) >= 21:
                        break
                    if len(yourHand) == 2:
                        print ("You have {}: \n 1. hit \n 2. stay \n 3. double".format(handValue(yourHand))) 
                    else:
                        print ("You have {}: \n 1. hit \n 2. stay ".format(handValue(yourHand))) 
                    action = raw_input('> ')
                    if 'hit' in action or '1' in action:
                        hit(deck, yourHand)
                    if 'stay' in action or '2' in action:
                        stay(yourHand)
                        break
                    #playerAction(action, yourHand, dealerHand, deck)
                    if 'double' in action or '3' in action:
                        hit(deck, yourHand)
                        print("Your Hand: {}".format(yourHand))
                        break
        
        if splitAction == 0:
        # deal the dealer if the play didnt choose to split, the dealer will be dealt
        # within the split function if the player chose to split
            dealTheDealer(dealerHand,deck)
            handOutcome(yourHand, dealerHand, 1)

# *******************************************************

runningCount = 0
print("How many decks do you want to use? Options are between 1 and 6.")
deck = bj_deck(int(raw_input('> ')))
shuffle(deck)
shoeCount = 0

while True:
    if shoeCount == 0:
        playGame(deck)
        shoeCount += 1
    else:
        print("Play another shoe?\n y\\n")
        choice = raw_input('> ')
        if 'y' in choice:
            print("How many decks do you want to use? Options are between 1 and 6")
            deck = bj_deck(int(raw_input('> ')))
            shuffle(deck)
            playGame(deck)
        else:
            print("Thanks for playing!")
            exit(0)
