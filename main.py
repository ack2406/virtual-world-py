from vworld.Organisms.Sheep import Sheep
from vworld.Organisms.Wolf import Wolf
from vworld.Organisms.Fox import Fox
from vworld.Organisms.Turtle import Turtle
from vworld.Organisms.Antelope import Antelope
from vworld.Organisms.Grass import Grass
from vworld.Organisms.SowThistle import SowThistle
from vworld.Organisms.Guarana import Guarana
from vworld.Organisms.Belladonna import Belladonna
from vworld.Organisms.Hogweed import Hogweed
from vworld.Organisms.CyberSheep import CyberSheep
from vworld.Organisms.Human import Human
from vworld.World import World
from vworld.Position import Position

import pygame

if __name__ == '__main__':

    pygame.init()

    win = pygame.display.set_mode((1440, 900))

    pygame.display.set_caption('Virtual World')

    world = World(30, 30)
    results = world.startGamePrompt(win)
    if results is None:
        exit(0)
    resultX, resultY = results
    if int(resultX) and int(resultY):
        world = World(int(resultX), int(resultY))
        world.populate()

    world.checkOutOfBounds()

    bg = pygame.image.load('vworld/images/bg.png')
    bg = pygame.transform.scale(bg, (1440, 900))
    sidebar = pygame.image.load('vworld/images/sidebar.jpg')
    sidebar = pygame.transform.scale(sidebar, (900, 900))

    pygame.font.init()

    clock = pygame.time.Clock()

    run = True
    win.blit(bg, (0, 0))
    win.blit(sidebar, (900, 0))
    world.drawWorld(win)
    world.showHumanControls(win)

    pygame.display.update()

    while run and True in [isinstance(org, Human) for org in world.organisms]:
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        world.makeTurn()

        win.blit(bg, (0, 0))
        win.blit(sidebar, (900, 0))
        world.showEvents(win)
        world.drawWorld(win)
        world.showHumanControls(win)

        pygame.display.update()

pygame.quit()
