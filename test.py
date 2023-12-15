import PyGameKit as pg

class Game(pg.Game):
    
    def start(self):
        self.x, self.y = 100, 100
        self.color = (100, 200, 255)
    
    def update(self):
        # pg.rect(pg.Rect(self.x, self.y, 100, 100), self.color, corner_radius=20, width=0)
        pg.ellipse((100, 100, 300, 700), (100, 200, 255))
        pg.update_screen()

Game((800, 600)).run()