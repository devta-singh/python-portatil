#vida_0.1c.py
import pygame
import numpy as np

pygame.init()

#damos ancho y alto a la pantalla
width, height = 500, 500

#creamos la pantalla con ancho y alto en pixeles
screen = pygame.display.set_mode((height, width))


bg = 25, 25, 25

#pintamos el fondo de la pantalla
screen.fill(bg)


#determinamos cuantas celdas en cada dirección
nxC, nyC = 25, 25

#establecemos las dimensiones de las celdas
dimCW = width / nxC
dimCH = height / nyC

# Estado de las celdas
gameState = np.zeros((nxC, nyC))

#bucle de ejecución
while True:

	#hacemos dos bucles for anidados para recorrer filas y columnas
	for y in range(0, nxC):
		for x in range(0,nyC):

				#creamos el polígono para esta celda de fila y columna
				poly = [((x)   * dimCW, y *dimCH),
						((x+1) * dimCW, y * dimCH),
						((x+1) * dimCW, (y+1) * dimCH),
						((x)   * dimCW, (y+1) * dimCH)]

				#dibujamos polígonos para cada celda, creando la cuadrícula
				pygame.draw.polygon(screen, (128,128,128), poly, 1)

	pygame.display.flip()

	pass
