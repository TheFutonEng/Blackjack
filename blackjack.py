# Going to try out making a blackjack game
# Let's see how feature rich it can become

from sys import exit
import random

# *******************************************************

def bj_deck(num):
    """Creates the full deck based on the number of decks the player wants to use"""
    if num < 1 and num > 6:
        exit(1)
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
    print deck
    return deck

# *******************************************************

def deal(deck, dealerHand, playerHand):
    for i in 2:
        yourHand.append(deck.pop())
        dealerHand.append(deck.pop())

    #print("Your Hand:/n{}".format(yourHand))
    #print("Dealer Hand:/n{}".format(dealerHand[1]))
    return yourHand, dealerHand, deck

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
    cardNum = 0
    for card in hand:
    # move all the aces to the back to make the logic below work better
        if 'a' in card:
            ace = hand.pop(cardNum)
            hand.insert(-1, ace)  
            cardNum += 1      

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
            if len(hand) == 2 and handValue == 10:
                handValue = 21
            elif handValue > 11:
                handValue += 1
            else:
                handValue += 11
    return handValue

# *******************************************************

def playerAction(action, playerHand, dealerHand, deck):
    """ This function is called each time the action is on the player """



# *******************************************************

def playGame(deck):
    """Main function used to play the game"""
    runningCount = 0
    shoe = False
    yourHand = []
    dealerHand = []

    while True:
    # While loop use to go through a hand start to finish, will exit after the shoe is hit
        for i in range(0,2):
        # Deal the dealer and player(s)
            if deck[0] == shoe:
                shoe = True
            yourHand.append(deck.pop(0))    
            count(yourHand[-1],runningCount)
            if deck[0] == shoe:
                shoe = True
            dealerHand.append(deck.pop(0))
            if len(dealerHand) == 2:
                count(dealerHand[-1],runningCount)
        
        print("Your Hand: /n {}".format(yourHand))
        print("Dealer Hand: /n {}, {}".format('xx',dealerHand[1]))
        
        if handValue(dealerHand) == 21:
        # Check if the dealer has blackjack and start a new hand if they do
            print "Dealer has Blackjack!"
            count(dealerHand[0], runningcount)
            continue
        else:
            if yourHand[0][:-1] == yourHand[1][:-1]:
            # Check if the player can split their hand and give them the option 
                print ("You have {}, hit, split or stay?".format(handValue(yourHand))) 
                action = raw_input('> ')
                if 'hit' in action:
                    yourHand.append(deck.pop(0))
                    count(yourHand[-1],runningCount)
                elif 'split' in action:
                # If a player splits, they get two hands to attempt to beat the dealer
                    yourHand2 = [yourHand.pop()]
                    yourHand.append(deck.pop(0))
                    count(yourHand[-1], runningCount)
                    yourHand2.append(deck.pop(0))
                    count(yourHand2[-1], runningCount)
                elif
            
# *******************************************************

print "How many decks do you want to use? Options are between 1 and 6."
deck = bj_deck(int(raw_input('> ')))
shuffle(deck)

playGame(deck)


