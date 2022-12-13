from player import Player
from card import Card

#Jenny's code (Human Class)

class Human(Player):
    """
    Child class of the Player class. Allows human player to play whatever card
    they would like to play and checks for errors.
    
    Attributes:
        name(str): Name of human player
        discard(list): Discard pile of cards 

    """
    def __init__(self, name):
        """
        Initializes the name attribute for the human player. 

        Args:
            name(str): Name of human player
        
        """
        #Super() (Required method/function)
        
        super().__init__(name)
        
    def playCards(self, discard):
        """
        
        Mechanism for user to play their selected card given user input. 
        Checks if selected card is playable. 
        
        Args:
            discard(list): Discard pile of cards 
        
        Returns:
            Returns human player's selected card (Card object). 
        
        """
        
        while True:
            cardinput = input("What card do you want to play? ")
            if len(cardinput) < 2:
                print("Invalid Input.")
                continue
            cardinput = cardinput.upper()
            facevalue = cardinput[:-1]
            suit = cardinput[-1:]
            selectedCard = Card(suit, facevalue)
            if len(self.cards) > 0:
                if selectedCard not in self.cards:
                    print("You do not have that card. Try another card.")
                    continue
            else:
                if selectedCard not in self.faceup:
                    print("You do not have that card. Try another card.")
                    continue
            #selected a card, but need to check if its playable
            #card = Card(suit, facevalue)
            if len(discard) == 0 or selectedCard >= discard[-1]:
                break
            else:
                print("You cannot play that card.")
                       

        if selectedCard in self.cards:
            self.cards.remove(selectedCard)
        elif selectedCard in self.faceup:
            self.faceup.remove(selectedCard)
        
        if len(self.cards) == 0 and len(self.faceup) == 0 and len(self.facedown) > 0:
            card = self.facedown.pop()
            self.faceup.append(card)
        
        return selectedCard
    
    def pickFaceUp(self):
        """
       
        Mechanism for user to pick their face up cards. Checks if user has 
        valid card in the first place and then appends card to face up list.
        
        Side effects: 
            Appends card to face up list. Prints status of game according to 
            user input. 
        
        """
        while len(self.faceup) < 1: #1 faceup card now
            print(self.cards)
            cardInput = input("Which card would you like to be face up? ")
            if len(cardInput) < 2:
                print("Invalid Card.")
                continue
            else:
                cardInput = cardInput.upper()
                #substring method, get all of the char except for the last char
                facevalue = cardInput[:-1]
                if facevalue not in Card.FACEVALUES:
                    print("Invalid facevalue.")
                    continue
                #get the last char of string
                suit = cardInput[-1:]
                if suit not in Card.SUITS:
                    print("Invalid suit.")
                    continue
            #have a valid card, but we do not know if player actually has that card
            selectedCard = Card(suit, facevalue)
            hasCard = False
            
            for card in self.cards:
                if card == selectedCard:
                    hasCard = True
                    self.faceup.append(card)
                    break
            
            if hasCard:
                self.cards.remove(selectedCard)
            else:
                print("You do not have that card. Try again. ")
    
    def playDrawPass(self):
        """
        
        Mechanism to allow user to choose if they would like to play, draw, 
        or pass during thei turn. 
        
        Returns:
            Returns player's choice (str).
        
        """
        while True:
            userInput = input("Play(p), Draw(d) of Pass(x) ? ")
            if len(userInput) == 0:
                print("Invalid Input.")
                continue
            userInput = userInput.lower()
            if userInput == "p":
                self.allowedToPass = True
                return "Play"
            elif userInput == "d":
                self.allowedToPass = True
                return "Draw"
            elif userInput == "x":
                if self.allowedToPass == True:
                    self.allowedToPass = False
                    return "Pass"
                else:
                    print("You cannot pass two rounds in a row.")
            else:
                print("Invalid input.")
                
                
        