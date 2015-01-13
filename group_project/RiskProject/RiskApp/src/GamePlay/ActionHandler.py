from ...models import GameConext
from ..BaseRuleSet import BaseRuleSet

class ActionHandler:

	#rules: BaseRuleSet module
	#player: player name passed as a string (Not the player object)
	#gc: GameContext object
	def __init__(self, rules, player, gc):
		self.rules = rules
		self.player = player
		self.gc = gc
