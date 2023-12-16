"""
PyGameKit - V1.0.0
An Abstraction on top of Pygame
Created to make Development on Pygame simpler for beginners

Originally Developed by: Prithak Adhikari

Github: https://github.com/PrithakADHI/PyGameKit

"""

import pygame
import sys

from pygame.sprite import Sprite
from pygame import *
import math
last_time = pygame.time.get_ticks()

class Game:
    def __init__(self, screen_size: tuple[int, int], vsync: bool = False, fullscreen: bool = False, fps: int = 60):
        pygame.init()
        if fullscreen:
            self.screen = pygame.display.set_mode(screen_size, vsync=vsync, flags=pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(screen_size, vsync=vsync, flags=pygame.SCALED)
        self.clock = pygame.time.Clock()
        self.fps = fps

        pygame.display.set_caption("PyGameKit Window")

    def start(self):
        # This method can be overridden by the user for initialization
        pass

    def update(self):
        # This method can be overridden by the user for the game loop
        pass

    def run(self):
        self.start()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            try:
                self.update()
            except Exception as e:
                print(f"Error in run: {e}")
                exit(1)
            self.clock.tick(self.fps)


# ----- All Fuunctions are listed below ------ #
def title(title):
    pygame.display.set_caption(title)

def update_screen():
    pygame.display.flip()

def background(color, screen=None):
    if screen == None:
        screen = pygame.display.get_surface()
    try:
        screen.fill(color)
    except Exception as e:
        print(f"Error in background: {e}")
        exit(1)

# ----- Drawing Functions -----
def line(start, end, color, width, screen=None):
    if screen == None:
        screen = pygame.display.get_surface()
    try:
        pygame.draw.line(screen, color, start, end, width)
    except Exception as e:
        print(f"Error in line: {e}")
        exit(1)

def rect(rect, color, corner_radius=0, width=0, screen=None): 
    if screen == None:
        screen = pygame.display.get_surface()
    try:
        
        if type(rect) == Rect:
            if width==0:
                pygame.draw.rect(screen, color, rect, border_radius=corner_radius)
            else:
                pygame.draw.rect(screen, color, rect, border_radius=corner_radius, width=width)
        else:
            pygame.draw.rect(screen, color, (rect[0], rect[1], rect[2], rect[3]), border_radius=corner_radius, width=width)
    except Exception as e:
        print(f"Error in rect: {e}")
        exit(1)

def circle(center, radius, color, screen=None):
    if screen == None:
        screen = pygame.display.get_surface()
    try:
        pygame.draw.circle(screen, color, center, radius)
    except Exception as e:
        print(f"Error in circle: {e}")
        exit(1)

def ellipse(rect, color, screen=None):
    if screen == None:
        screen = pygame.display.get_surface()
    try:
        if type(rect) == Rect:
            if len(rect) == 2:
                raise ValueError("The Co-ordinates must have 4 elements")
            pygame.draw.ellipse(screen, color, rect)
        else:
            if len(rect) == 2:
                raise ValueError("The Co-ordinates must have 4 elements")
            pygame.draw.ellipse(screen, color, (rect[0], rect[1], rect[2], rect[3]))
    except Exception as e:
        print(f"Error in ellipse: {e}")
        exit(1)

def arc(rect, start, stop, color, screen=None):
    if screen == None:
        screen = pygame.display.get_surface()
    try:
        if type(rect) == Rect:
            if len(rect) == 2:
                raise ValueError("The Co-ordinates must have 4 elements")
            pygame.draw.arc(screen, color, rect, start, stop)
        else:
            if len(rect) == 2:
                raise ValueError("The Co-ordinates must have 4 elements")
            pygame.draw.arc(screen, color, (rect[0], rect[1], rect[2], rect[3]), start, stop)
    except Exception as e:
        print(f"Error in arc: {e}")
        exit(1)

# ----- Imaging Functions -----
def load_image(filename: str, colorkey=None):
    try:
        image = pygame.image.load(filename)
        image = image.convert()
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, RLEACCEL)
        return image
    except Exception as e:
        print(f"Error in load_image: {e}")
        exit(1)

def display_image(surface: Surface, rect, screen=None):
    if screen == None:
        screen = pygame.display.get_surface()
    try:
        if type(rect) == pygame.Rect:
            screen.blit(surface, rect)
        else:
            if len(rect) == 2:
                screen.blit(surface, (rect[0], rect[1]))
            elif len(rect) == 4:
                surface = pygame.transform.smoothscale(surface, (rect[2], rect[3]))
                screen.blit(surface, (rect[0], rect[1], rect[2], rect[3]))
            else:
                raise ValueError("Invalid rect argument")
    except Exception as e:
        print(f"Error in display_image: {e}")
        exit(1)

# ----- Transform Functions -----
def scale(surface: Surface, size: tuple[int, int]):
    try:
        surface = pygame.transform.scale(surface, size)
    except Exception as e:
        print(f"Error in Scale: {e}")
        exit(1)
    return surface

def rotate(surface: Surface, angle: int):
    try:
        surface = pygame.transform.rotate(surface, angle)
    except Exception as e:
        print(f"Error in rotate: {e}")
        exit(1)
    return surface

def flip(surface: Surface, flip_x:bool = False, flip_y:bool = False):
    try:
        surface = pygame.transform.flip(surface, flip_x, flip_y)
    except Exception as e:
        print(f"Error in flip: {e}")
        exit(1)
    return surface

def smoothscale(surface: Surface, size: tuple[int, int], screen=None):
    if screen == None:
        screen = pygame.display.get_surface()
    try:
        surface = pygame.transform.smoothscale(surface, size)
    except Exception as e:
        print(f"Error in smoothscale: {e}")
        exit(1)
    return surface

# ----- Key Handling Functions -----
def keypress(keycode):
    try:
        keys = pygame.key.get_pressed()

        # Check if the specified key is pressed
        if keys[getattr(pygame, f'K_{keycode}')]:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error in keypress: {e}")
        exit(1)
    
def delayed_keypress(keycode: str, delay):
    global last_time
    current_time = pygame.time.get_ticks()
    try:
        keys = pygame.key.get_pressed()
        if keys[getattr(pygame, f'K_{keycode.lower()}')] and current_time - last_time > delay:
            last_time = current_time
            return True
    
        return False
    except Exception as e:
        print(f"Error in delayed_keypress: {e}")
        exit(1)


# ----- Mouse Handling Functions -----
        
def mouse_getpos():
    try:
        return pygame.mouse.get_pos()
    except Exception as e:
        print(f"Error in mouse_getpos: {e}")
        exit(1)

def mouse_pressed():
    try:
        return pygame.mouse.get_pressed()
    except Exception as e:
        print(f"Error in mouse_pressed: {e}")
        exit(1)

def delayed_mouse_pressed(delay):
    global last_time
    current_time = pygame.time.get_ticks()
    try:
        if mouse_pressed() and current_time - last_time > delay:
            last_time = current_time
            return mouse_pressed()

        return (False, False, False)
    except Exception as e:
        print(f"Error in delayed_mouse_pressed: {e}")
        exit(1)

def mouse_mov(): # pygame.mouse.get_rel()
    try:
        return pygame.mouse.get_rel()
    except Exception as e:
        print(f"Error in move_mov: {e}")
        exit(1)

def mouse_setpos(co: tuple[int, int]):
    try:
        pygame.mouse.set_pos(co)
    except Exception as e:
        print(f"Error in mouse_setpos: {e}")
        exit(1)

def mouse_setvis(value: bool):
    try:
        pygame.mouse.set_visible(value)
    except Exception as e:
        print(f"Error in mouse_setvis: {e}")
        exit(1)

def mouse_getvis():
    try:
        return pygame.mouse.get_visible()
    except Exception as e:
        print(f"Error in mouse_getvis: {e}")
        exit(1)