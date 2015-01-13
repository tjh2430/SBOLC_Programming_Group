from ...models import Player, Territory
from random import randint

#TODO: implemented using a mapping of functions to their parameters which will then be executed
# when the execute() function is called; will require that all functions have a duplicate which accepts
# a GameInstance object as an additional parameter. The functions will then be executed (in order?)
# when execute is called
#
# Note: use operator.method caller to execute the functions

class GameAction:

	def addArmies(numArmies, territory):

	def removeArmies(numArmies, territory):

	def attack(srcTerr, destTerr, numAttack, numDefend):

	def execute(gameInstance):