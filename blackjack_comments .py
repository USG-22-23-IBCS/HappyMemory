import random

class Card:

    def __init__(self, suit, name):
        self.suit = suit
        self.name = name
        #definining the values of suit and name

    def getName(self):
        return self.name
    #defining the Name method

    def getSuit(self):
        return self.suit
    #defining the Suit method

    def getCard(self):
        return [self.suit, self.name]
    #defining the Card method 

class Deck:
    #defining the class Deck 

    def __init__(self):
        self.cards = []
        suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
        #defining the suit, and giving the options of the suits that the program will produce
        for s in suits:
            #loops through the suit list
            for i in range(1, 14):
                #means that i can be only in range from 1 to 14 
                if i == 1:
                    name = "Ace"
                elif i == 11:
                    name = "Jack"
                #elif means else if, basically matching different numbers with different names of the cards in the deck. 
                elif i == 12:
                    name = "Queen"
                elif i == 13:
                    name = "King"
                else:
                    name = str(i)
                    #if the number won't be as any listed above, the name will be any other number in range from 1 to 14

                C = Card(s, name)
                self.cards.append(C)
                #adds the element to the list

    def getCards(self):
        return self.cards
    #useless      

    def dealCard(self):
        newCard = random.choice(self.cards)
        #defining the function newCard which means that the computer will deal a random card
        self.cards.remove(newCard)
        #basically this method removes the card that was dealt from the deck
        return newCard

def calcHandValue(hand):
    total = 0
    # total is the value of your hand before you have been dealt a card
    for h in hand:
        name = h[1]
        if name == "Ace":
            total = total + 11
            #this means that if the name of the card was Ace, the total value of the card will be total+11, because the Ace value is 11
            if total > 21:
                total = total - 10
        elif name == "King" or name == "Queen" or name == "Jack" :
            total = total + 10
            #here the the value of the King, Queen and Jack is 10, thus the total will be equal to the total + 10
        else:
            total = total + int(name)
        
    return total
        #here return total means that the program will output the total result

def main():

    print("Welcome to Blackjack!\n")
    #program outputs "Welcome to Blackjack!", \n means line break 

    D = Deck()

    userHand = [D.dealCard().getCard(), D.dealCard().getCard()]
    #defines the cards that should be outputed for user
    dealerHand = [D.dealCard().getCard(), D.dealCard().getCard()]
    #defines the cards that should be outputed for dealer

    print("Dealer hand:")
    print(dealerHand)
    #prints the random cards for the dealer
    print("")
    print(userHand)
    print("Your hand's value is :" + str(calcHandValue(userHand)))
    print("")

    while True:
        bust = False
        #creating bust as a boolean function, which is always false unless proven otherwise
        option = input("Type 1: Hit  or 2: Stand\n")
        if option == "1":
            #if the user inputs '1' then the program will add a new random card to the user's deck, using function append
            userHand.append(D.dealCard().getCard())
        else:
            break
            #if user inputs other number, then the program stops here, that's why function break is used 

        if calcHandValue(userHand) > 21:
            #this means that if the total value of user's cards is bigger than 21, the user is busted  
            bust = True
            print("User bust!")
            print ("Dealer wins")
            #thus, if the user is busted, dealer wins, that's why we are printing 'Dealer wins' as well
            break
              
        print("")
        print(userHand)
        print("Your hand's value is :" + str(calcHandValue(userHand)))
        print("")

    if bust == False :
        #but if the user didn't bust, which we describe by using boolean expression if bust== False, then the dealer will deal more cards
    
        print("")
        print("Dealer hand:")
        print(dealerHand)
        print("Dealer hand's value is :" + str(calcHandValue(dealerHand)))
        print("")
    
        while True:
            if calcHandValue(dealerHand) < 17:
                print("Dealer hits!\n")
                dealerHand.append(D.dealCard().getCard())
                print("Dealer hand:")
                print(dealerHand)
                print("Dealer hand's value is :" + str(calcHandValue(dealerHand)))
                print("")
            else:
                print("Dealer stands!\n")
                break
            if calcHandValue(dealerHand) > 21:
                print("Dealer bust!")
                print("User wins")
                break
        
            
        if calcHandValue(dealerHand) > calcHandValue(userHand):
        #this means that if the dealer has a bigger value of cards than the user than dealer wins, thus we print 'dealer wins' afterwards 
            print("Dealer wins")
        else:
            print("User wins")
            
        
       
       
            
        
            

if __name__ == "__main__":
    main()
