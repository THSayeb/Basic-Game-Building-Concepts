import pygame

def main():
    pygame.init()
    
    Height, Width = 500, 500
    screen = pygame.display.set_mode((Width, Height))
    pygame.display.set_caption("Color Changing Sprite")  

    colors = {
        'red': pygame.Color('red'),
        'blue': pygame.Color('blue'),
        'green': pygame.Color('green'),
        'lightblue': pygame.Color('lightblue'),
        'yellow': pygame.Color('yellow')
    }
    current_color = colors['red']
    x, y = 20, 30
    height, width = 60, 60
    clock = pygame.time.Clock()
    
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        if pressed[pygame.K_UP]: y -= 3 
        if pressed[pygame.K_DOWN]: y += 3 

        x = min(max(0, x), Width - width)
        y = min(max(0, y), Height - height)

        if x == 0: current_color = colors['blue']
        elif x == Width - width: current_color = colors['green']
        elif y == 0: current_color = colors['lightblue']
        elif y == Height - height:  current_color = colors['yellow']
        else: current_color = colors['red']

        screen.fill((0, 0, 0)) 
        pygame.draw.rect(screen, current_color, (x, y, width, height))
        pygame.display.flip()
        clock.tick(150) 
    pygame.quit()

if __name__ == "__main__":
    main()