

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
        
            
        