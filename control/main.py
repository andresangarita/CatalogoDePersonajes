from ..model.Personaje import *
from ..control.Builder import *
from ..view.VPrincipal import *
from ..view.VPartes import *

def buildOrco():
	orco = OrcoBuilder()
	directorOrco = Director()
	directorOrco.setBuilder(orco)
	orcoo = directorOrco.getOrco()
	game_loop_partes("Orco")

def buildHumano():
	humano = HumanoBuilder()
	directorHumano = Director()
	directorHumano.setBuilder(humano)
	humanoo = directorHumano.getHumano()
	game_loop_partes("Humano")	

def buildElfo():
	elfo = ElfoBuilder()
	directorElfo = Director()
	directorElfo.setBuilder(elfo)
	elfoo = directorElfo.getElfo()
	game_loop_partes("Elfo")

if __name__ == '__main__':
	game_loop()
	quitGame()
 
