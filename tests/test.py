import PyGameKit as pg

class Game(pg.Game):
    
    def start(self):
        self.x, self.y = 100, 100
        self.color = (100, 200, 255)
    
    def update(self):
        img = pg.load_image("cat.png")
        img = pg.flip(img, flip_x=True, flip_y=True)
        pg.display_image(img, (self.x, self.y, 200, 200))
        pg.update_screen()

Game((800, 600)).run()