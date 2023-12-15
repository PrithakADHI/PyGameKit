import pygame

screen = pygame.display.set_mode(( 800, 600 ))

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pygame.draw.arc(screen, ( 255, 0, 0 ), ( 100, 100, 200, 200 ), 0, 3.14, 2)

    pygame.display.update()