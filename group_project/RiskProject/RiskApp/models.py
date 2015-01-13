from django.db import models

class Territory (models.Model):

	#Name of territory
	name = models.CharField(max_length=32)

	#Region it lives under
	region = models.CharField(max_length=32)
	
	#Which territories can units move to?
	adjacent = models.ManyToManyField(Territory)
	
	#Player that controls it
	owner = models.ForeignKey(Player, verbose_name='owner')	
	
	#Number of soldiers occupying
	strength = models.SmallIntegerField()
	
	def __str__(self):
		return self.name+'('+self.owner+')'
	

class TerritoryCard (models.Model):

	#Territory
	name = models.ForeignKey(Territory)

	# "Infantry","Cavalry", or "Artillery" (Base game rules)
	type = models.CharField(max_length=32)

class GameMap (models.Model):

	#Name of map type	
	mapTitle = models.CharField(max_length=32)

	#Regions contained within map
	regions = models.ManyToManyField(Region)
	
	#All territories within map
	territoryGraph = models.ManyToManyField(Territory)

	#Link to map image to be used
	gameMapFileURL = models.URLField(max_length=200)

	#TODO: No equivalent of a text list, unless we want a separate object for colors, perhaps have colors separated by spaces to parse it better
	availablePlayerColors = models.CharField(max_length=200)
	
	def __init__(self):
		return self.mapTitle
	
class GameInstance (models.Model):
	ruleSet = models.ForeignKey(RuleSet)
	players = models.ManyToManyField(Player)
	gameMap = models.ForeignKey(GameMap)
	context = models.ForeignKey(GameContext)

	#TODO: Add methods (How to access attributes of FK objects)
	

class Player (models.Model):
	
	#Copied from unique user account name
	userName = models.CharField(max_length=32)
	
	#Dependent on GameMap specs
	color = models.CharField(max_length=32)
	
	#Territory cards owned by player
	cards = models.ManyToManyField(TerritoryCard)

	def __str__(self):
		return self.userName+'('+self.color+')'

class GameInstance (models.Model):

	#Unique ID per instance of game
	gameID = models.AutoField(primary_key=True)
	
	#URL link to config file to be used to init Regions/Territories
	mapconfig = models.URLField(max_length=200)
	
	#Players participating in game
	players = models.ManyToManyField(Player)
	
	#URL link to config file for rules of game
	ruleset = models.URLField(max_length=200)
	
	#Instances of territories within game
	gamemap = models.ManyToManyField(Territory)
	
	def __str__(self):
		return "game"+str(self.gameID)
		





