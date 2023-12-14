# PyGameKit

<p> Created as an Abstraction of Pygame to make development a bit easier for begineer Python Programmers. </p>
<p> Uses Object-Oriented Concepts to create an Abstraction. </p>

<h3> Documentation </h3>
<p> Before we overview the functionality of PyGameKit. Here are some basic codes: </p>
<h4> Simple Program to draw a Rect </h4>

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