import PyGameKit as pg

class Game(pg.Game):
    
    def start(self):
        self.x, self.y = 100, 100
        self.color = (100, 200, 255)
    
    def update(self):
        pg.rect((self.x, self.y, 50, 50), self.color)
        pg.update_screen()

Game((800, 600)).run()