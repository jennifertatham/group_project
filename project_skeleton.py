class Card:
    """
    Create each card in a standard deck of cards and assign value to each card
    as it pertains to the game, Palace.
    
    Attributes:
        Suit(Str): The suit of the card (H, S, C, and D)
        Facevalue(Str): The value of the card from 2 to Ace 
        Othercard(str): The card on the top of the playing deck.
    """
    SUITS = ["H", "S", "C", "D"]
    FACEVALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    
    def __init__(self, suit, facevalue):
        """
        Initialize each card attribute and assign values to each card.
        
        Args:
            Suit(Str): The suit of the card (H, S, C, and D)
            Facevalue(Str): The value of the card from 2 to Ace
        
        Side effects: 
            Creates attributes for each card.  
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
        """
        Create an informal string representation of the card.
        
        Returns:
            Informal string representation of the card.
        """
        return f"{self.facevalue}{self.suit}"
    
    def __ge__(self, othercard):
        """
        Determine if one can play their card based on the current playing card.
        Exceptions for 2's and 10's.
        
        Args:
            othercard(str): The card on the top of the playing deck.
            
        Returns:
            Returns boolean value.
        
        """
        if self.value == 2 or self.value == 10:
            return True
        elif othercard.value == 2 or othercard.value == 10:
            return False
        else:
            return self.value >= othercard.value
        
    def __eq__(self, othercard):
        """
        Check if a player has a card whose suit or facevalue matches the playing card.
        
        Args:
            othercard(str): The card on the top of the playing deck.
            
        Returns:
            Returns boolean value. 
        """
        if self.facevalue != othercard.facevalue:
            return False
        elif self.suit != othercard.suit:
            return False
        else:
            return True

class Player:
    """
    Create the rules of the game for all players.
    
    Attributes:
        name(str): The name of the player
        cards(str): A list of the cards each player has.
        faceup(str): A list of the faceup cards each player has.
        facedown(str): A list of the facedown cards each player has.
        quantity(str): The quantity of cards a player has.
        cardinput(str): Card being played
        cardlist(str):The list of the players cards in their hand.
              
    """
    
    def __init__(self, name):
        """
        Initializes the name and cards of a player.
        
        Args:
            name(str): The name of the player
            cards(str): A list of the cards in the hand of each player
            faceup(str): A list of the faceup cards each player has.
            facedown(str): A list of the facedown cards each player has.
        
        Side effects:
            Creates empty lists of cards for the player. 
        """
        self.name = name
        self.cards = []
        self.faceup = []
        self.facedown = []
    
    def __str__(self):
        """
        Create an informal string representation of each players cards, which 
        includes the cards in their hand as well as their faceup and facedown
        cards.
        
        Returns:
            A display of the player's cards.
        """
        display = self.name + "\n"
        display += self.cards + "\n"
        display += self.faceup + "\n"
        for x in len(self.facedown):
            display += "x"
        display += "\n"
        
        return display
    
    def play(self, topCard):
        """
        Create a mechanism for player to play the game. 
        
        Args:
            topCard(str): The card on the top of the deck.
        """
        pass 
    
    def has_enough_cards(self, quantity, cardinput, cardlist):
        """
        Check how many cards a player has in their hand.
        
        Args:
            Quantity(int): The quantity of cards a player has.
            Cardinput(str): The card being played
            Cardlist(str): The list of the players cards in their hand.
        
        Returns:
            A boolean of True or False depending on if the user has enough cards.
            
        """
        count = 0
        for card in cardlist:
            if card == cardinput:
                count += 1
        
        if quantity <= count:
            return True
        else:
            return False
    
    def deal(self, cards):
        """
        Deals player their cards and gives them 3 to facedown. 
        
        Args:
            Cards(str): A list of cards each player has.
        
        Side effects:
            Appends 3 cards to the facedown pile and 6 cards to players hands.
        """
        for i in range(3):
            card = cards.pop()
            self.facedown.append(card)
        
        #we now have 6 cards left
        for card in cards:
            self.cards.append(card)
            
    def pickFaceUp(self):
        pass

class Human(Player):
    """
    Inherits the player class and allows human player to manuver game.
    
    Attributes:
        name(str): Name of the human player
        topCard(str): The card on the top of the deck.
    """
    def __init__(self, name):
        """
        Create a name attribute for the human player.

        Args:
            name(str): Name of human player
            
        Side effects:   
            Initializes the human player with their name attribute.
        """
        super().__init__(name)
        
    def play(self, topCard):
        """
        Allow human player to play their cards. Troubleshoot if player plays 
        wrong card.
        
        Args:
            topCard(str): The card on the top of the deck.
       
        Side effects:
            Prints messages based on the card a user inputs. 
        """
    
    def pickFaceUp(self):
        """
        Allow users to choose which three cards they would like faced up. 
        
        Side effects:
            Appends cards to faceup list only if the card is in the human 
            player's hand.
        """
       

class AI(Player):
    """
    Inherit the player class and create AI player that can manuever game.
    
    Attributes:
        topCard(str): The card on the top of the deck.

    """
    def __init__(self):
        """ 
        Initialize the AI player.
            
        Side effects:   
            Initializes the AI player with the name "Testudo."
        """
        super().__init__("Testudo")
        
    def play(self, topCard):
        """
        Allow "Testudo", the AI, to play its hand and create mechanisms 
        for it to play all cards.
        
        Args:
            topCard(str): The card on the top of the deck.
        
        Returns:
            The selected card that the AI has chosen.
        """
                        
    def pickFaceUp(self):
        """
        Creates the faceup cards for the AI. 
        
        Side effects:
            Appends faceup cards to the faceup list.
        """

class Game:
    """
    Mechanism for playing the game. Create instances of human and AI classes.
    Create the deck and draws cards. Deal cards.
    """
    
    def __init__(self):
        """
        Create instances of human and AI player classes. 
        """
        
    def createDeck(self):
        """
        Creates stuffled deck for user.
        
        Side effects:
            Appends cards to card deck and shuffles cards.
        """
        
    def draw(self):
        """
        Allows user to draw card from deck.
        
        Side effects:
            Pops card from deck.
            
        Returns:
            A card.
        """
        
    def deal(self):
        """
        Deals 9 cards to human and AI. 
        
        Side effects:
            Appends cards to list for human player and AI player.   
        """
    
    def newGame(self):
        """
        Creates a new game.
        """

if __name__ == "__main__":
    """
    Executes program.
    """
        