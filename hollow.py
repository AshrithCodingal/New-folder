import pygame
import random
pygame.init()
screen = pygame.display.set_mode((500,500))

done= False
color = (random.randint(1,225),random.randint(1,225),random.randint(1,225))
while not done:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
              done = True

    pygame.draw.circle(screen,(random.randint(1,225),random.randint(1,225),random.randint(1,225)),(300,300),50,3)

    pygame.display.flip()
