import pygame
from pygame.locals import *
import random
import math

#initialize pygame
pygame.init()
pygame.font.init()

# Define size of the screen
WIDTH = 1400
HEIGHT = 785
SCREEN_SIZE = WIDTH, HEIGHT
SCREEN = pygame.display.set_mode(SCREEN_SIZE)

# Add background image
BACKGROUND_IMAGE = pygame.image.load("assets/images/wooden_background.jpg")
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, SCREEN_SIZE)

# Font choice
FONT = pygame.font.Font('Tsuchigumo.otf', 50)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Get objects
APPLE = pygame.image.load("assets/images/fruits/apple.png")
BANANA = pygame.image.load("assets/images/fruits/banana.png")
BOMB = pygame.image.load("assets/images/fruits/bomb.png")
CHERRY = pygame.image.load("assets/images/fruits/cherry.png")
ICE_CUBE = pygame.image.load("assets/images/fruits/ice_cube.png")
MANGO = pygame.image.load("assets/images/fruits/mango.png")
PEAR = pygame.image.load("assets/images/fruits/pear.png")
STRAWBERRY = pygame.image.load("assets/images/fruits/strawberry.png")

clock = pygame.time.Clock()

# game variables
# Get object type
object_type = ["apple", "banana", "bomb", "cherry", "ice_cube", "mango", "pear", "strawberry"]
object_data = {}
OBJECT_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"