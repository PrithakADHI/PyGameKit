import PyGameKit as pg

class MyGame(pg.Game):
    def start(self):
        pg.title("Tests")
        self.catx = 0
        self.caty = 0
        self.cat = pg.load_image("cat.png")
    def update(self): # Game Loop
        pg.background((0, 0, 0))

        mx, my = pg.mouse_getpos()
        mb = pg.mouse_pressed()

        if mb[0]:
            self.catx, self.caty = mx - (200 / 2), my - (200 / 2)

        
        pg.display_image(self.cat, (self.catx, self.caty, 200, 200))

        pg.update_screen()

MyGame((800, 600), vsync=True, fps=60).run()

"""
Same Program in PyGame:

import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600), vsync=True)
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
    
    screen.blit( pygame.transform.smoothscale(cat, (200, 200)), (100, 100) )

    pygame.display.flip()
    clock.tick(60)

"""