import pygame
pygame.init()

screen = pygame.display.set_mode((400, 500))

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(33,33,66,66))
    pygame.display.flip()