# Same Program in PyGame:

import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600), vsync=True, flags=pygame.SCALED)
clock = pygame.time.Clock()

catx = 0
caty = 0
cat = pygame.image.load("cat.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    mx, my = pygame.mouse.get_pos()
    mb = pygame.mouse.get_pressed()

    if mb[0]:
        catx, caty = mx - (200 / 2), my - (200/2)
    
    screen.blit( pygame.transform.smoothscale(cat, (200, 200)), (catx, caty) )

    pygame.display.flip()
    screen.fill((0, 0, 0))
    clock.tick(60)