# PyGameKit

<p> Created as an Abstraction of Pygame to make development a bit easier for begineer Python Programmers. </p>
<p> Uses Object-Oriented Concepts to create an Abstraction. </p>

<h3> Documentation </h3>
<p> Before we overview the functionality of PyGameKit. Here are some basic codes: </p>
<h4> Simple Program to draw a Rect </h4>
<pre>
import PyGameKit as pg

class MyGame(pg.Game):
    def start(self):
        self.x, self.y = 100, 100
        self.color = (100, 200, 255)
    
    def update(self):
        pg.rect( (self.x, self.y, 100, 100), self.color )
        pg.update_screen()

MyGame( (800, 600) ).run()
</pre>