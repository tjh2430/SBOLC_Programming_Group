from django.db import models

#Map Objects

class Territory (models.Model):

	#Name of territory
	name = models.CharField(max_length=32)
	
	#Which territories can units move to?
	adjacent = models.ManyToManyField(Territory)
	
	#Player that controls it
	owner = models.ForeignKey(Player, verbose_name='owner')	
	
	#Number of soldiers occupying
	strength = models.SmallIntegerField()
	
	def __str__(self):
		return self.name+'('+self.owner+')'
	
class Region (models.Model):
	
	#Name of region
	name = models.CharField(max_length=32)
	
	#Territories that are members of this region
	territories = models.ManyToManyField(Territory)

	#How many extra soldiers is total ownership worth?
	bonus = models.SmallIntegerField()
	
	def __str__(self):
		return self.name


class Player (models.Model):
	
	#Copied from unique user account name
	userName = models.CharField(max_length=32)
	
	#Dependent on GameMap specs
	color = models.CharField(max_length=32)
	
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
		





