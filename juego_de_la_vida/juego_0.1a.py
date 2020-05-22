#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pygame.locals import *
import pygame
import time

pygame.init()
# Display
screen = pygame.display.set_mode((800, 600))
# Window titlebar
bg = 128,128,128
screen.fill(bg)

pygame.display.set_caption('Bullet dodger')
pygame.display.set_icon(pygame.image.load('bullet.png'))
time.sleep(1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False


pygame.quit()