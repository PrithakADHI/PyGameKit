import PyGameKit as pg

class MyGame(pg.Game):
    def start(self):
        pg.title("Tests")
        self.catx = 0
        self.caty = 0
    def update(self): # Game Loop
        pg.background((0, 0, 0))

        cat = pg.load_image("cat.png")

        mx, my = pg.mouse_getpos()
        mb = pg.mouse_pressed()

        if mb[0]:
            self.catx, self.caty = mx - (200 / 2), my - (200 / 2)

        
        pg.display_image(cat, (self.catx, self.caty, 200, 200))

        pg.update_screen()

MyGame((800, 600), True).run()