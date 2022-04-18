import pygame
from network import Network
from player2 import Player
from dot import *
from load import load_map
from spritesheet import Spritesheet
from tiles import *
import threading


width = 1280
height = 720
canvas = pygame.Surface((width, height))
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
spritesheet = Spritesheet('spritesheet.png')

n = None
players = []
p1 = None
level = -1
map = None
walls = []
dots = []
home = ()
run = True


def set_network():
    global n
    if n is None:
        n = Network()
    return n.getP()


def redrawWindow():
    global win, p1, players, map, walls
    win.fill((180, 181, 254))
    canvas.fill((180, 181, 254))
    map.draw_map(canvas)
    win.blit(canvas, (64, 32))
    for dot in dots:
        dot.draw(win)
    for player in players:
        if not player.current_player == p1.current_player:
            if player.level == p1.level:
                player.draw(win)
    for wall in walls:
        pygame.draw.rect(win, (0, 0, 0), wall)
    p1.draw(win)
    pygame.display.update()


def update_players(player, clock):
    global players, run
    while run:
        clock.tick(60)
        try:
            players = n.send(player)
        except:
            pass


def update_dots():
    global dots
    for dot in dots:
        try:
            dot.move()
        except:
            pass


def load_level(num):
    global level, map, walls, dots, home, p1
    level = num
    level_data = load_map(level)
    map = TileMap(level_data['map'], spritesheet)
    walls = level_data['walls']
    dots = level_data['dots']
    home = level_data['home']
    end = pygame.Rect(0, 0, 0, 0)
    p1.set_level(level, home, end)


def play_multi():
    global p1, level, players, n, stop, run
    run = True
    clock = pygame.time.Clock()
    data = set_network()
    p1 = data[0]
    level = data[1]
    threading.Thread(target=update_players,
                     args=(p1, clock),
                     ).start()
    load_level(level)
    while run:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_b]:
            clock.tick(1)
        else:
            clock.tick(60)
        p1.move(walls, dots)
        update_dots()
        redrawWindow()

        if keys[pygame.K_j]:
            load_level(1)
        if keys[pygame.K_k]:
            load_level(2)
        if keys[pygame.K_l]:
            load_level(3)
        if keys[pygame.K_SEMICOLON]:
            load_level(4)
        if keys[pygame.K_ESCAPE]:
            run = False
            n.disconnect()
            n = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                n.disconnect()
                n = None
                pygame.quit()