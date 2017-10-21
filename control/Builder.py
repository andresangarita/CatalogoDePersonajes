from ..model.Personaje import *

class Director:
	
	__builder = None

	def setBuilder(self,builder):
		self.__builder = builder

	def getOrco(self):
		orco = Orco()

		casco = self.__builder.getCasco()
		orco.setCasco(casco)

		arma = self.__builder.getArma()
		orco.setArma(arma)
		
		armadura = self.__builder.getArmadura()
		orco.setArmadura(armadura)

		return orco 

	def getHumano(self):
		humano = Humano()

		casco = self.__builder.getCasco()
		humano.setCasco(casco)

		arma = self.__builder.getArma()
		humano.setArma(arma)
		
		armadura = self.__builder.getArmadura()
		humano.setArmadura(armadura)

		return humano

	def getElfo(self):
		elfo = Elfo()

		casco = self.__builder.getCasco()
		elfo.setCasco(casco)

		arma = self.__builder.getArma()
		elfo.setArma(arma)
		
		armadura = self.__builder.getArmadura()
		elfo.setArmadura(armadura)

		return elfo

class Builder:

	def getCasco(self):pass
	def getArma(self):pass
	def getArmadura(self):pass

class OrcoBuilder(Builder):

	def getCasco(self):
		casco = CascoOrco()
		casco.cubrirCabeza()
		return casco
	def getArma(self):
		arma = ArmaOrco()
		arma.accion()
		return arma
	def getArmadura(self):
		armadura = ArmaduraOrco()
		armadura.cubrir()
		return armadura

class HumanoBuilder(Builder):

	def getCasco(self):
		casco = CascoHumano()
		casco.cubrirCabeza()
		return casco
	def getArma(self):
		arma = ArmaHumano()
		arma.accion()
		return arma
	def getArmadura(self):
		armadura = ArmaduraHumano()
		armadura.cubrir()
		return armadura

class ElfoBuilder(Builder):

	def getCasco(self):
		casco = CascoElfo()
		casco.cubrirCabeza()
		return casco
	def getArma(self):
		arma = ArmaElfo()
		arma.accion()
		return arma
	def getArmadura(self):
		armadura = ArmaduraElfo()
		armadura.cubrir()
		return armadura	