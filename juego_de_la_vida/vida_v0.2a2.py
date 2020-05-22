#vida_0.2a2.py
import pygame
import numpy as np
import time

pygame.init()

#damos ancho y alto a la pantalla
width, height = 500, 500

#creamos la pantalla con ancho y alto en pixeles
screen = pygame.display.set_mode((height, width))


bg = 25, 25, 25

#pintamos el fondo de la pantalla
screen.fill(bg)


#determinamos cuantas celdas en cada dirección
#nxC, nyC = 25, 25
tam = 4
nxC, nyC = int(width / tam), int(width / tam)


#establecemos las dimensiones de las celdas
dimCW = width / nxC
dimCH = height / nyC

# Estado de las celdas. Vivas = 1; Muertas = 0;
gameState = np.zeros((nxC, nyC))


# Inicializamos algunos datos

# Automata palo 
gameState[5, 3] = 1;
gameState[5, 4] = 1;
gameState[5, 5] = 1;


# Automata movil
gameState[21, 21] = 1;
gameState[22, 22] = 1;
gameState[22, 23] = 1;
gameState[21, 23] = 1;
gameState[20, 23] = 1;


# Control de ejecución.
pauseExect = False

#bucle de ejecución
while True:

	newGameState = np.copy(gameState)

	# repintamos el fondo (borramos la pantalla)
	screen.fill(bg)
	#time.sleep(0.001)


	# Registramos eventos de teclado y ratón.
	ev = pygame.event.get()

	for event in ev:
		if event.type == pygame.KEYDOWN:
			pauseExect = not pauseExect

		mouseClick = pygame.mouse.get_pressed()
		#print(mouseClick) #obtiene el vector de botones del raton (no pulsado = 0; pulsados = 1)

		if sum(mouseClick) > 0:
			posX, posY = pygame.mouse.get_pos()
			celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
			#newGameState[celX, celY] = 1 #cambia a 1 activo el estado de la celda
			newGameState[celX, celY] = not mouseClick[2] #toma la lectura del boton izquierdo del raton y la niega


	#hacemos dos bucles for anidados para recorrer filas y columnas
	for y in range(0, nxC):
		for x in range(0,nyC):

			#controlamos si se han de actualizar las reglas
			if not pauseExect:

				# Calculamos el número de vecinos cercanos.
				n_neigh = gameState[(x - 1) % nxC, (y - 1)  % nyC] + \
				          gameState[(x)     % nxC, (y - 1)  % nyC] + \
				          gameState[(x + 1) % nxC, (y - 1)  % nyC] + \
				          gameState[(x - 1) % nxC, (y)      % nyC] + \
				          gameState[(x + 1) % nxC, (y)      % nyC] + \
				          gameState[(x - 1) % nxC, (y + 1)  % nyC] + \
				          gameState[(x)     % nxC, (y + 1)  % nyC] + \
				          gameState[(x + 1) % nxC, (y + 1)  % nyC]


				# Regla #1 : Una célula muerta con exactamente 3 vecinas vivas, "revive".

				if gameState[x, y] == 0 and n_neigh == 3:
					newGameState[x, y] = 1

				# Regla #2 : Una célula viva con menos de 2  o más de 3 vecinas vivas, "muere"
				elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
					newGameState[x, y] = 0

			#creamos el polígono para esta celda de fila y columna
			poly = [((x)   * dimCW, y * dimCH),
					((x+1) * dimCW, y * dimCH),
					((x+1) * dimCW, (y+1) * dimCH),
					((x)   * dimCW, (y+1) * dimCH)]

			#dibujamos polígonos para cada celda, creando la cuadrícula
			if newGameState[x, y] == 0:
				pygame.draw.polygon(screen, (128,128,128), poly, 1)#solo los bordes
			else:
				pygame.draw.polygon(screen, (255,255,255), poly, 0)#relleno solido

	
	# Actualizamos el estado del juego
	gameState = np.copy(newGameState)

	pygame.display.flip()

	pass
