
class Player:
    """
    Parent class of AI and Human
    
    Attributes:
        name(str): name of the player    
        cards(str): card that's in player's hand
        faceup(str): card facing up
        facedown(str): card facing down
        discard(str): discarded card
        
    """
    
    def __init__(self, name):
        """
        initialize player's name and card
        
        Args:
            name(str): name of the player    
            cards(str): card that player has
            faceup(str): card facing up
            facedown(str): card facing down
        
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
        shows player's name and cards in player's hand, facing up card and facing down cards
        
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
        """
        Create a mechanism for player to play the game. 
        
        Args:
            topCard(str): The card on the top of the deck.
        """
    
    def deal(self, cards):
        """
        list of cards that the player just got when the game started
        
        Args:
            cards: cards that player has
            
        Side effects:
            Appends 3 cards to the facedown pile and 6 cards to players hands.
        """
        card = cards.pop()
        self.facedown.append(card)
        
        #we now have 4 cards left
        for card in cards:
            self.cards.append(card)
            
    def pickFaceUp(self):
        pass
    
    def hasCards(self):
        """
        how many cards player has
        
        Args:
            cards: card that player has
            faceup: card facing up
            facedown: card facing down
        
        return: number of cards that are greater than 0
        """
        numCards = len(self.cards)
        numCards += len(self.faceup)
        numCards += len(self.facedown)
        
        return numCards > 0
    
    def hasPlayableCard(self, discard):
        """
        check if the player has a card that is playable, can be used
        
        Args:
            discard: discarded card
        
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
        """ player can choose whether to play draw or pass on their turn. 
        """
        pass 
    
    def draw(self, card):
        """ draws card 

        Args:
            card (_type_): _description_
            
        """
        self.cards.append(card)
    
