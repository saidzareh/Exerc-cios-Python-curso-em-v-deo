import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex.23 musica.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()