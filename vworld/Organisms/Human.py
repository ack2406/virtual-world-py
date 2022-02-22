import pygame

from vworld.Animal import Animal
from vworld.Position import Position
from pygame.locals import *
import sys


class Human(Animal):
    def __init__(self, position, world):
        super().__init__(5, 4, position, 'H', 'Human', world)

    def giveBirth(self, position):
        return Human(position, self.world)

    def action(self):
        # direction = input('Human action (move with "WSAD", use special ability with R)\n')

        pygame.event.clear()
        while True:
            event = pygame.event.wait()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    direction = 'w'
                    break
                if event.key == K_s:
                    direction = 's'
                    break
                if event.key == K_a:
                    direction = 'a'
                    break
                if event.key == K_d:
                    direction = 'd'
                    break
                if event.key == K_r:
                    direction = 'r'
                    break
                if event.key == K_f:
                    direction = 'f'
                    break

        if direction == 'w':
            newPosition = Position(self.position.x, self.position.y - 1)
        elif direction == 's':
            newPosition = Position(self.position.x, self.position.y + 1)
        elif direction == 'a':
            newPosition = Position(self.position.x - 1, self.position.y)
        elif direction == 'd':
            newPosition = Position(self.position.x + 1, self.position.y)
        elif direction == 'r':
            if self.immortality == -5:
                self.immortality = 5
                self.world.events.append(f'Special ability has been activated.')
            elif self.immortality > 0:
                self.world.events.append(f'Special ability is active.')
            elif self.immortality:
                self.world.events.append(f'Special ability is on cooldown.')
            self.action()
            return
        elif direction == 'f':
            self.world.saveGame()
            self.action()
            return
        else:
            newPosition = None

        if not newPosition or not self.world.positionOnBoard(newPosition):
            newPosition = None

        if newPosition:
            otherOrganism = self.world.getOrganismFromPosition(newPosition)
            if otherOrganism:
                if type(self) is type(otherOrganism):
                    self.reproduce()
                else:
                    if otherOrganism.attack(self):
                        self.position = newPosition
            else:
                self.position = newPosition

        if self.immortality != -5:
            if self.immortality == 1:
                self.world.events.append(f'Special ability just turned off.')
            if self.immortality == -4:
                self.world.events.append(f'Special ability is ready.')
            self.immortality -= 1
