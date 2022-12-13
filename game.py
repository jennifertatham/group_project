
import random
from card import Card
from human import Human
from AI import AI
import argparse

#Alisha Hukmani worked on this entire file
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
        