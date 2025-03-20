import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))
screen.fill((255,255,255))

Green = (0,255,0)
pygame.draw.circle(screen, Green, (300,300), 66)
pygame.draw.circle(screen, Green, (100,100), 50, 3)
pygame.display.update()

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
pygame.quit()