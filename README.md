# PyGameKit

<p> Created as an Abstraction of Pygame to make development a bit easier for begineer Python Programmers. </p>
<p> Uses Object-Oriented Concepts to create an Abstraction. </p>

# Documentation
<p> Before we overview the functionality of PyGameKit. Here are some basic codes: </p>

## Simple Program to draw a Rect

```python
import PyGameKit as pg

class Game(pg.Game):
    
    def start(self):
        self.x, self.y = 100, 100
        self.color = (100, 200, 255)
    
    def update(self):
        pg.rect((self.x, self.y, 50, 50), self.color)
        pg.update_screen()

Game((800, 600)).run()
```

<p> Here, we are Inheriting from the PyGameKit Library's Game Class, Overriding the start and update functions, and then
PyGameKit creates a game loop by itself through the run method down below. The Developer now doesn't have to remember
as much boiler-plate code as before in pygame. If they have some knowledge in OOP, they can grasp this pretty easily. </p>

<p> The Game Function has a init function which has two values: the screen size and whether you want vsync on or off. To
turn on Vsync you can: </p>

```python
Game((800, 600), vsync=True).run()
```

<p> Declaration of variables is simple. Declare all the variables you need in the start function using: </p>

```python
self.[variable_name] = value
```

<p> This ensures that the variable is transferred over to the update function too. </p>

## Key Features

<h3> delayed_keypress </h3>
<p> This function checks if a specified key is pressed after a certain delay. This can be useful in many scenarios where the normal keypress function is outputting too fast. You can specify your own delay here. </p>

```python
from PyGameKit import delayed_keypress

if delayed_keypress('SPACE', 500):  # Check if SPACE key is pressed after a delay of 500 milliseconds
    # Your code here

```

<h3> delayed_mouse_press </h3>
<p> Same thing as the delayed_keypress but for mouse presses. </p>

```python
from PyGameKit import delayed_mouse_pressed

if delayed_mouse_pressed(500)[0]:  # Check if the left mouse button is pressed after a delay of 500 milliseconds
    # Your code here

```

<h3> Displaying Images is easier now </h3>
<p> Now, all the images loaded in PyGameKit will normally follow the rect behaviour. It uses pygame.transform.smoothscale to fit the image into the given rect. </p>

```python
# This is the same as example.py
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
```


<h3> Compatibility with PyGame </h3>
<p> You can write the same kind of PyGame Programs with PyGameKit with no problems.</p>

```python
import PyGameKit as pg
screen = pg.display.set_mode((800, 600))

while True:
    for event in pg.events.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    
    pg.draw.rect((100, 100, 200, 200), (100, 200, 255))

```

And this works as intented. <br>

## PyGameKit Functions, their Functionalities and their Examples.
<h3> Screen Functions </h3> 
<h4> title </h4> Changes the title of the Game Window. <br>By Default it is: PyGameKit Window.

```python
# [...]
PyGameKit.title("Example")
# [...]
```
<h4> update_screen </h4> Equivalent to pygame.display.flip() <br> Makes the screen visible.

```python
# [...]
PyGameKit.update_screen()
# [...]
```
<h4> background </h4>
<p> Argument list: color, screen(optional) </p>
Changes the background of the screen to a certain color. The color is the same as pygame.

```python
PyGameKit.background( (0, 0, 0) ) # Black Background
```

<h3> Drawing Functions </h3>
<h4> line </h4>
<p> Argument list: start, end, color, width, screen(optional) </p>
<p> Draws a line from start to end with width. </p>

```python
PyGameKit.line( (100, 100), (200, 200), (100, 200, 255), 5, surface ) # Draws a blue line from 100, 100 to 200, 200 on the screen called 'surface'
```

<h4> rect </h4>
<p> Argument list: rect, color, corner_radius, width, screen(optional) </p>
<p> Draws a rect with the given color, corner_radius and width </p>
<p> Note: If width is 0, then the width argument is ignored. </p>

```python
PyGameKit.rect( (100, 100, 200, 200), (100, 200, 255), 5, 10)
```

<h4> circle </h4>
<p> Argument list: center, radius, color, screen(optional) </p>
<p> Draws a circle in the center co-ordinate with the radius and color. </p>

```python
PyGameKit.circle( (100, 100), 50, (100, 200, 255) )
```

<h4> ellipse </h4>
<p> Argument list: rect, color, screeen(optional) </p>
<p> Draws an ellipse around the rect with the given color. </p>

```python
PyGameKit.ellipse(( 100, 100, 200, 300 ), (100, 200, 255))
```

<h4> arc </h4>
<p> Argument List: rect, start, stop, color, screen(optional) </p>

```python
PyGameKit.arc( (100, 100, 200, 200), 0, 180 )
```

## Imaging Functions

<h4> load_image </h4>
<p> Argument list: filename, colorkey </p>

Loads the image and stores it into the given variable. If a color key is given, returns a transparent image. 


```python
img = PyGameKit.load_image("cat.png")
```

<h4> display_image </h4>
<p> Argument list: surface, rect, screen(optional) </p>

Displays the before-mentioned image on a rect. It can also display any surface as required.

```python
img = PyGameKit.load_image("cat.png")
PyGameKit.display_image(img, (100, 100, 200, 200)) # <- The rect can also have two arguments, in which case it won't be scaled. 
```

## Transform Functions

<h4> scale </h4>
<p> Argument list: surface, size </p>
Scales the surface into the required size. This is the non-smooth variant.

```python
img = PyGameKit.load_image("cat.png")
img = PyGameKit.scale(img, (200, 200))
PyGameKit.display_image(img, (100, 100))
```

<h4> smoothscale </h4>
<p> Argument list: surface, size </p>
Scales the surface into the required size. This is the smooth variant.

```python
img = PyGameKit.load_image("cat.png")
img = PyGameKit.smoothscale(img, (200, 200))
PyGameKit.display_image(img, (100, 100))
```

<h4> rotate </h4>
<p> Argument list: surface, angle