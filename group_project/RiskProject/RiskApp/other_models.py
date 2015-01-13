class Region (models.Model):
	
	#Name of region
	name = models.CharField(max_length=32)
	
	#Territories that are members of this region
	territories = models.ManyToManyField(Territory)

	#How many extra soldiers is total ownership worth?
	bonus = models.SmallIntegerField()
	
	def __str__(self):
		return self.name

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

class ActionHandler (models.Model):
	rules = models.ForeignKey(RuleSet)
	#TODO: Isn't it more appropriate to make this a FK?
	playerID = models.CharField(max_length=32)
	gameContext = models.ForeignKey(GameContext)

	#TODO: class methods

class GameAction (models.Model):
	#TODO: Shouldn't there be a link to the ActionHandler?

	