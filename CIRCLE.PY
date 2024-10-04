import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))

done= False

while not done:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
              done = True

    pygame.draw.circle(screen,(255,30,50),(300,300),50)

    pygame.display.flip()

