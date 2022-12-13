#Final Project File for Submission
from player import Player
from card import Card
import random 
from human import Human
from AI import AI
import argparse

#Rachel Lee
class Player:
    """
    Parent class of AI and Human
    
    Attributes:
        name(str): name of the player    
        cards(list): cards that's in player's hand
        faceup(list): cards facing up
        facedown(list): cards facing down
        discard(list): discarded cards
        
    """
    
    def __init__(self, name):
        """
        initialize player's name and card
        
        Args:
            name(str): name of the player    
            cards(list): cards that player has
            faceup(list): cards facing up
            facedown(list): cards facing down
        
        Side effects:
            Creates empty lists of cards for the player. 
            
        """
        self.name = name
        self.cards = []
        self.faceup = []
        self.facedown = []
        self.allowedToPass = True
    
    def __str__(self):
        """
        shows player's name and cards in player's hand, facing up cards and facing down cards
        
        Returns:
            A display of the player's cards.
        
        """
        display = self.name + "\n"
        display += str(self.cards) + "\n"
        display += str(self.faceup) + "\n"
        for x in range(len(self.facedown)):
            display += "x"
        display += "\n"
        
        return display
    
    def playCards(self, discard):
        pass
    
    def deal(self, cards):
        """
        list of cards that the player just got when the game started
        
        Args:
            cards(list): cards that player has
            
        Side effects:
            Appends 1 card to the facedown pile and 3 cards to players hands.
        """
        card = cards.pop()
        self.facedown.append(card)
        
    
        for card in cards:
            self.cards.append(card)
            
    def pickFaceUp(self):
        pass
    
    def hasCards(self):
        """
        how many cards player has
        
        return: number of cards that are greater than 0
        """
        numCards = len(self.cards)
        numCards += len(self.faceup)
        numCards += len(self.facedown)
        
        return numCards > 0
    
    def hasPlayableCard(self, discard):
        """
        check if the player has a card that is playable, or can be used
        
        Args:
            discard(list): discarded cards
        
        returns: true or false depending on length of discarded card
        """
        if len(discard) == 0:
            return True
            #player can play any card
        for card in self.cards:
            if card >= discard[-1]:
                #player has at least one card they can play
                return True
        #player does not have any mroe cards in their hand
        if len(self.cards) == 0:
            for card in self.faceup:
                if card >= discard[-1]:
                    return True
        #no card could be played
        return False
    
    def playDrawPass(self):
        """ 
        player can choose whether to play draw or pass on their turn. 
        """
        pass 
    
    def draw(self, card):
        """ draws card 
        Args:
            card (list): cards that's in player's hand
        
        sideeffects:
            appends each drawn cards to player's hand
            
        """
        self.cards.append(card)


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


#Jenny's code (AI class)

class AI(Player):
    """
    Child class of the Player class. Allows AI to randomly play its turn and
    also creates mechanism for it to pick face up cards. 
    
    Attributes:
        name(str): Name of AI; optional parameter
        discard(list): Discard pile of cards
    """
    
    #Optional parameter (Required method/function)
    def __init__(self, name = "Testudo"):
        """
        Initiatlizes the name attribute for the AI player. 
        
        Args:
            name(str): Name of AI; optional parameter
        
        """
        super().__init__(name)
        
    def playCards(self, discard):
        """
        Mechanism for the AI to randomly play the game. 
        
        Args:
            discard(list): Discard pile of cards
        
        Returns:
            Returns AI player's selected card (Card object). 
        
        """
        if not self.hasPlayableCard(discard):
            print(f"{self.name} has no playable cards.")
            self.cards.extend(discard)
            return None #did not play a card so none
        selectedCard = None
        if len(self.cards) > 0:
            while True:
                card = random.choice(self.cards)
                if len(discard) == 0 or card >= discard[-1]:
                    selectedCard = card
                    break
        #check face up cards
        elif len(self.faceup) > 0:
            while True:
                card = random.choice(self.faceup)
                if len(discard) == 0 or card >= discard[-1]:
                    selectedCard = card
                    break
        else: #need to pick from facedown cards
            card = self.facedown.pop()
            self.faceup.append(card)
            return self.playCards(discard) 
        
        if selectedCard in self.cards:
            self.cards.remove(selectedCard)
        elif selectedCard in self.faceup:
            self.faceup.remove(selectedCard)
            
        
        return selectedCard
                    
        
            
    def playDrawPass(self):
        """
        Mechanism that creates random chance that AI plays, draws, or passes. 
        
        Returns:
            Returns AI's choice to play, draw, or pass (str). 
        
        """
        chance = random.randint(1, 100)
        #50 percent chance they can play a card
        if chance <= 50:
            self.allowedToPass = True
            return "Play"
        elif self.allowedToPass == False:
            self.allowedToPass = True
            return "Draw"
        elif chance <= 80:
            #30 percent chance selected to draw
            self.allowedToPass = True
            return "Draw"
        else: 
            #20 percent chance to pass
            self.allowedToPass = True
            return "Pass"
    
    def pickFaceUp(self):
        """
        Mechanism that takes 3 cards and puts it in the AI's faceup pile.
        
        Side effects: 
            Appends 3 cards to the faceup pile. 
        
        """
        card = self.cards.pop()
        self.faceup.append(card)

#Rachel Lee
class Card:
    """determines which cards are higher and what cards are special
    
    Attributes:
        suit(str): card symbols 'club', 'diamond', 'hearts', 'spade'
        facevalue(str): 2-10, 'J','Q','K','A'
        
    """
    
    SUITS = []
    FACEVALUES = []
    
    
    def __init__(self, suit, facevalue):
        """
        initialized suit and facevalue, creates value for 'J',"q",'K',"A"
        
        Attributes:
            suit(str): card symbols 'club', 'diamond', 'hearts', 'spade'
            facevalue(str): 2-10,'J','Q','K','A'
            
        """
        self.suit = suit
        self.facevalue = facevalue
        
        if self.facevalue == "A":
            self.value = 14
        elif self.facevalue == "K":
            self.value = 13
        elif self.facevalue == "Q":
            self.value = 12
        elif self.facevalue == "J":
            self.value = 11
        else:
            self.value = int(self.facevalue)
                
        
    def __str__(self):
        """gives us each card (informal string representation)
        
        returns: card formatted facevalue suit
        
        """
        return f"{self.facevalue}{self.suit}"
    
    def __repr__(self):
        """debugging purposes: gives us each card
        
        returns: card formatted facevalue suit
        
        """
        return f"{self.facevalue}{self.suit}"
    
    def __ge__(self, othercard):
        """comparing the cards of AI player and human player (exception for 2 and 10)
        
        Args:
            othercard: othercard being compared
            
        returns: true or false depending on the comparison of two cards
        """
        if self.value == 2 or self.value == 10:
            return True
        elif othercard.value == 2 or othercard.value == 10:
            return False
        else:
            return self.value >= othercard.value
        
    def __eq__(self, othercard):
        """use this to check if player has playable card
        
        Args: 
            othercard: othercard being compared
            
        returns: true or false after checking the cards
        """
        if self.facevalue != othercard.facevalue:
            return False
        elif self.suit != othercard.suit:
            return False
        else:
            return True
    
    
#Alisha Hukmani worked on this file
class Game:
    """Creates the functionality of the card game that allows the game to come together
    
    Attributes:
        name(str): name of human player
        humanPlayer(Human object): creates the human player
        AIplayer(AI object): creates the AI player
    """
    
    def __init__(self, name):
        """Creates the game and initalizes the attributes of the game

        Args:
            name (str): name of human player
            
        """
        self.humanPlayer = Human(name)
        self.AIplayer = AI()
        self.newGame() 
        
    def createDeck(self):
        """ Creates functinality to access the deck and use it by reading and parsing through textfile. Randomly shuffles the cards in deck
        
        Side effect: 
            Appends cards to deck
        """
        self.deck = []
        with open("cards.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("#"):
                    continue
                line = line.strip()
                suit = line[-1]
                facevalue = line[:-1]
                card = Card(suit, facevalue)
                self.deck.append(card)
                Card.SUITS.append(suit)
                Card.FACEVALUES.append(facevalue)
        
        random.shuffle(self.deck)
        
    def draw(self):
        """Draws card from deck
        
        Side effect: 
            Pops cards to deck
        
        Returns:
            Card that was taken out of deck
        """
        if len(self.deck) > 0:
            card = self.deck.pop()
            return card
        else:
            return None
        
    def deal(self):
        """Deals starting cards to players
        
        Sife effects:
            Appends the cards to player's hands(list)
        """
        humancards = [] 
        
        numCards = 5 #can change if wanna play with more cards
        
        for i in range(numCards):
            card = self.draw()
            humancards.append(card)
        self.humanPlayer.deal(humancards)
        
        AIcards = []
        
        for i in range(numCards):
            card = self.draw()
            AIcards.append(card)
        self.AIplayer.deal(AIcards)
    
    def isGameOver(self):
        """Check to see if game is over by assessing if players have cards 
        
        Return:
            boolean: if the game is over return true, if the game is not over, return false
        """
        if not self.humanPlayer.hasCards():
            #game is over
            return True
        elif not self.AIplayer.hasCards():
            return True
        else:
            return False
            #game is not over
            
    def playRound(self):
        """Creates a single round of the game
        
        Side effect: Prints out status of the game, depending on player's decision
        """
        print(self.humanPlayer)
        if not self.humanPlayer.hasPlayableCard(self.discard):
            print(f"{self.humanPlayer.name} has no playable cards.")
            self.humanPlayer.cards.extend(self.discard)
            self.discard = []
            self.humanPlayer.allowedToPass = True
        else:
            action = None
            while True:
                action = self.humanPlayer.playDrawPass()
                if action == "Draw" and len(self.deck) == 0:
                    #no more cards on the deck
                    print("There are no cards in the deck.")
                else:
                    #valid selection
                    break

            if action == "Play":
                playedCard = self.humanPlayer.playCards(self.discard)
                self.discard.append(playedCard)
                if playedCard.value == 10:
                    self.discard = []
                print(f"{self.humanPlayer.name} played {playedCard}.")
            elif action == "Draw":
                card = self.deck.pop()
                self.humanPlayer.draw(card)
                print(f"{self.humanPlayer.name} drew {card}.")
            else:
                print(f"{self.humanPlayer.name} has decided to pass.")
            
        input("Press any key to continue.")
        print()
        print(self)
        
        
        #AI's turn
        
        if not self.isGameOver():
            if not self.AIplayer.hasPlayableCard(self.discard):
                print(f"{self.AIplayer.name} has no playable cards.")
                self.AIplayer.cards.extend(self.discard)
                self.discard = []
                self.AIplayer.allowedToPass = True
            else:
                action = None
                while True:
                    action = self.AIplayer.playDrawPass()
                    if action == "Draw" and len(self.deck) == 0:
                        #no more cards on the deck
                        print("There are no cards in the deck.")
                    else:
                        #valid selection
                        break
                if action == "Play":
                    playedCard = self.AIplayer.playCards(self.discard)
                    self.discard.append(playedCard)
                    if playedCard.value == 10:
                        self.discard = []
                    print(f"{self.AIplayer.name} played {playedCard}.")
                elif action == "Draw":
                    card = self.deck.pop()
                    self.AIplayer.draw(card)
                    print(f"{self.AIplayer.name} drew {card}.")
                else:
                    print(f"{self.AIplayer.name} has decided to pass.")
            
            input("Press any key to continue.")
            print()
            print(self)
            
    
    def __repr__(self):
        """Representation of the current state of the game 
        
        Return:
            gameState(str): status of the game
        """
        gameState = "===========================================\n"
        gameState += f"Remaining cards: {len(self.deck)}\n"
        gameState += f"Cards in discard pile: {len(self.discard)}\n"
        if len(self.discard) > 0:
            gameState += f"Top card on pile: {self.discard[-1]}\n"
        else:
            gameState += "Top card on pile: None\n"
            #no top card on discard pile, so player can play any card
        gameState += "===========================================\n"
        return gameState 
    
    def newGame(self):
        """Creates a new game
        """
        self.createDeck()
        self.deal()
        self.humanPlayer.pickFaceUp()
        self.AIplayer.pickFaceUp()
        self.discard = [] 
        #pile of cards, if player cannot play any cards they have to pick up this pile and add to their hand
    
    def winner(self):
        """Determines the winner of the game
        
        Side effect:
            Prints out a response according to who won
        """
        if not self.humanPlayer.hasCards():
            print(f"{self.humanPlayer.name} wins! Yay.")
        elif not self.AIplayer.hasCards():
            print(f"{self.AIplayer.name} wins! Boo.")
        
def runGame(name):
    """Allows the game to run

    Args:
        name(str): takes in the name of the human player
    """
    game = Game(name)
    print(game)
    while not game.isGameOver():
        game.playRound()
    game.winner()
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name", type = str, help="Name is required.")
    args = parser.parse_args()
    runGame(args.name)
        