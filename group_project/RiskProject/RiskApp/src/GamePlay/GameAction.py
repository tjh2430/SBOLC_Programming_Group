from enum import Enum, unique

from ...models import Player, Territory
from random import randint

#
# Defines all of the possible game actions
#
@unique
class Action(Enum):

# EXPLAINATION OF ACTIONS
#
# AddArmies             Adds the specified number of armies to the given territory    
# RemoveArmies          Removes the specified number of armies from the given territory
# MoveArmies            Move the specified number of armies from the source territory to the destination
# Attack                Perform an attack from the source territory to the destination with the specified number of armies for attack and defense
# DrawTerritoryCard     Remove a territory card from the territory card deck and give it to the specified player
# DrawActionCard        Remove a action card from the action card deck and give it to the specified player
# GiveArmiesToPlayer    Assign the specified number of armies to the given player for placement (such as at the start of a player's turn)
# PlaceArmies           Place the specified number of armies from the player's current pool of armies onto the given territory
# AssignTerritory       Make the specified player the owner of the territory
# TurnInCardSet         Turn in the card set consisting of the listed territory cards and award the corresponding bonus to the player
# EndTurn               Ends the current player's turn
# EndGame               Ends the current game

#    
#   Actions                  Parameters
#
    AddArmies = 1            # Number of armies (int), territory name (string)
    RemoveArmies = 2         # Number of armies (int), territory name (string)
    MoveArmies = 3           # Number of armies (int), source territory name (string), destination territory name (string)
    Attack = 4               # Number of attack armies (int), number of defending armies (int), source territory name (string), destination territory name (string)
    DrawTerritoryCard = 5    # Player id (string)
    DrawActionCard = 6       # Player id (string)
    GiveArmiesToPlayer = 7   # Player id (string), number of armies (int)
    PlaceArmies = 8
    AssignTerritory = 9      # Player id (string), territory name (string)
    TurnInCardSet = 10        # Player id (string), cards (tuple: territory card)
    EndTurn = 11             # [None]
    EndGame = 12             # [None]

#
# Represents an action, or series of actions, to be performed. Note that
# actions will be interpretted and performed in the order in which they they
# are added to the GameAction object (i.e. calling addArmies() followed by
# attack() means add armies and then attack; calling these methods in reverse
# will cause the attack to happen first followed by adding armies).
#
class GameAction:

    def __init__(self):
        self.actions = []

    def addArmies(self, numArmies, territory):
        self.actions.append((AddArmies, (numArmies, territory)))
        
    def removeArmies(self, numArmies, territory):
        self.actions.append((RemoveArmies, (numArmies, territory)))
        
    def moveArmies(self, numArmies, sourceTerritory, destTerritory):
        self.actions.append((MoveArmies, (numArmies, sourceTerritory, destTerritory)))
    def attack(self, numAttacking, numDefending, sourceTerritory, destTerritory):
        self.actions.append((Attack, (numAttacking, numDefending, sourceTerritory, destTerritory)))
    def drawTerritoryCard(self, playerId):
        self.actions.append((DrawTerritoryCard, (playerId)))
        
    def drawActionCard(self, playerId):
        self.actions.append((DrawActionCard, (playerId)))
        
    def giveArmiesToPlayer(self, playerId, numArmies):
        self.actions.append((GiveArmiesToPlayer, (playerId, numArmies)))
        
    def placeArmies(self, playerId, territory):
        self.actions.append((PlaceArmies, (playerId, territory)))
        
    def turnInCardSet(self, playerId, cards):
        self.actions.append((TurnInCardSet, (playerId, cards)))
        
    def endTurn(self):
        self.actions.append((EndTurn))
        
    def endGame(self):
        self.actions.append((EndGame))
        
    # Returns the list containing all of the actions and corresponding
    # parameters stored in this GameAction
    #
    # Ex: [(AddArmies, (3, 'Brazil')), (EndTurn)] -> Adds three armies to Brazil
    # and then ends the current player's turn
    def getActions(self):
        return self.actions
