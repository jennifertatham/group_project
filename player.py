
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
    