from django.db import models

# Create your models here.

class Player (models.Model):
	userName = models.CharField(max_length=32)
	def __str__(self):
		return self.userName

class Game (models.Model):
	gameID=models.AutoField(primary_key=True)
	players=models.ManyToManyField(Player)
	gameMap=models.ManyToManyField("Territory")
	def __str__(self):
		return "game"+str(self.gameID)

class Territory (models.Model):
	gameID = models.ForeignKey(Game, verbose_name="game")
	name = models.CharField(max_length=32)
	strength = models.SmallIntegerField()
	owner = models.ForeignKey(Player, verbose_name="owner")	
	adjacent = models.ManyToManyField("self")
	def __str__(self):
		return str(self.gameID)+"_"+self.name
