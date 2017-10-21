from .Casco import *
from .Armadura import *
from .Arma import *
from .Singleton import *

class Personaje:

	def setCasco(self):
		pass

	def setArmadura(self):	
		pass

	def setArma(self):	
		pass

class Humano(Personaje,Singleton):
	
	def __init__(self):
		self.__casco = None
		self.__armadura = None
		self.__arma = None
	
	def setCasco(self, casco):
		self.__casco = casco

	def setArmadura(self, armadura):	
		self.__armadura = armadura

	def setArma(self, arma):	
		self.__arma = arma	

class Elfo(Personaje,Singleton):
	
	def __init__(self):
		self.__casco = None
		self.__armadura = None
		self.__arma = None
	
	def setCasco(self, casco):
		self.__casco = casco

	def setArmadura(self, armadura):	
		self.__armadura = armadura

	def setArma(self, arma):	
		self.__arma = arma	

class Orco(Personaje,Singleton):

	def __init__(self):
		self.__casco = None
		self.__armadura = None
		self.__arma = None
	
	def setCasco(self, casco):
		self.__casco = casco

	def setArmadura(self, armadura):	
		self.__armadura = armadura

	def setArma(self, arma):	
		self.__arma = arma	
