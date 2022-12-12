from player import Player
import random 

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
            