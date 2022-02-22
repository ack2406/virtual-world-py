import random

from vworld.Position import Position
import vworld.Organisms as o
import pygame


class World:
    def __init__(self, x, y):
        self._sizeX = x
        self._sizeY = y
        self._organisms = []
        self._events = []
        self._turn = 0
        self._separator = '.'
        self._images = {'A': 'ant', 'B': 'bel', 'C': 'cyb', 'F': 'fox', '/': 'gra',
                        'G': 'gua', '$': 'hog', 'H': 'hum', 'S': 'she', '*': 'sow',
                        'T': 'tur', 'W': 'wolf'}

    @property
    def sizeX(self):
        return self._sizeX

    @sizeX.setter
    def sizeX(self, value):
        self._sizeX = value

    @property
    def sizeY(self):
        return self._sizeY

    @sizeY.setter
    def sizeY(self, value):
        self._sizeY = value

    @property
    def organisms(self):
        return self._organisms

    @organisms.setter
    def organisms(self, value):
        self._organisms = value

    @property
    def events(self):
        return self._events

    @events.setter
    def events(self, value):
        self._events = value

    @property
    def turn(self):
        return self._turn

    @turn.setter
    def turn(self, value):
        self._turn = value

    @property
    def separator(self):
        return self._separator

    @separator.setter
    def separator(self, value):
        self._separator = value

    @property
    def images(self):
        return self._images

    @images.setter
    def images(self, value):
        self._images = value

    def makeTurn(self):
        self.organisms.sort(key=lambda organism: organism.initiative, reverse=True)

        organismsAmount = len(self.organisms)
        i = 0
        while i < organismsAmount:
            if self.organisms[i]:
                self.organisms[i].action()
                organismsAmount = len(self.organisms)
            i += 1

        self.turn += 1

    def showEvents(self, win):
        for i, event in enumerate(self.events):
            print(event)
            myfont = pygame.font.SysFont('Comic Sans MS', 20)
            textsurface = myfont.render(event, False, (255, 255, 255))
            win.blit(textsurface, (920, 30 + i * 30))
        self.events.clear()

    def saveGame(self):
        self.events.append('Saved game.')
        with open('save.txt', 'w', encoding='utf-8') as f:
            f.write(f'{self.turn} {self.sizeX} {self.sizeY}\n')
            for org in self.organisms:
                f.write(f'{org.symbol} {org.position.x} {org.position.y} {org.strength} {org.immortality}\n')

    def loadGame(self):
        availableOrganisms = {'A': o.Antelope.Antelope, 'B': o.Belladonna.Belladonna, 'C': o.CyberSheep.CyberSheep,
                              'F': o.Fox.Fox, '/': o.Grass.Grass, 'G': o.Guarana.Guarana, '$': o.Hogweed.Hogweed,
                              'H': o.Human.Human, 'S': o.Sheep.Sheep, '*': o.SowThistle.SowThistle,
                              'T': o.Turtle.Turtle, 'W': o.Wolf.Wolf}
        with open('save.txt', 'r', encoding='utf-8') as f:
            settings = f.readline().split()
            self.turn = int(settings[0])
            self.sizeX = int(settings[1])
            self.sizeY = int(settings[2])
            for line in f:
                symbol, x, y, strength, immortality = line.split()
                x = int(x)
                y = int(y)
                pos = Position(x, y)
                newOrganism = availableOrganisms[symbol](pos, self)
                newOrganism.strength = int(strength)
                newOrganism.immortality = int(immortality)
                self.organisms.append(newOrganism)

    def addOrganism(self, organism):
        self.organisms.append(organism)

    def getOrganismFromPosition(self, position):
        for organism in self.organisms:
            if organism and organism.position == position:
                return organism
        return None

    def positionOnBoard(self, position):
        return 0 <= position.x < self.sizeX and 0 <= position.y < self.sizeY

    def getNeighboringPositions(self, position):
        result = []
        for y in range(-1, 2):
            for x in range(-1, 2):
                neighboringPosition = Position(position.x + x, position.y + y)
                if self.positionOnBoard(neighboringPosition) and (x or y):
                    result.append(neighboringPosition)
        return result

    def getNeighboringJumpingPositions(self, position):
        result = []
        for y in range(-2, 3):
            for x in range(-2, 3):
                neighboringPosition = Position(position.x + x, position.y + y)
                if self.positionOnBoard(neighboringPosition) and (x or y):
                    result.append(neighboringPosition)
        return result

    def getFreePositions(self, position):
        positions = self.getNeighboringPositions(position)
        return [pos for pos in positions if not self.getOrganismFromPosition(pos)]

    def getPositionClosestTo(self, thisPosition, otherPosition):
        difference = thisPosition - otherPosition
        newPos = Position(thisPosition.x, thisPosition.y)
        if difference.x > 0:
            newPos.x -= 1
        elif difference.x < 0:
            newPos.x += 1

        if difference.y > 0:
            newPos.y -= 1
        elif difference.y < 0:
            newPos.y += 1
        return newPos

    def getClosestHogweed(self, pos):
        potentialHogweeds = [organism.position for organism in self.organisms if
                             isinstance(organism, o.Hogweed.Hogweed)]
        if len(potentialHogweeds):
            hogPosition = potentialHogweeds[0]
            for position in potentialHogweeds:
                if hogPosition.getDistance(pos) > position.getDistance(pos):
                    hogPosition = position
        else:
            return None
        return hogPosition

    def checkOutOfBounds(self):
        self.organisms = [org for org in self.organisms if self.positionOnBoard(org.position)]

    def showHumanControls(self, win):

        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        result = 'Human action:'
        textsurface = myfont.render(result, False, (255, 255, 255))
        win.blit(textsurface, (920, 670))
        result = 'W - up'
        textsurface = myfont.render(result, False, (255, 255, 255))
        win.blit(textsurface, (920, 700))
        result = 'S - down'
        textsurface = myfont.render(result, False, (255, 255, 255))
        win.blit(textsurface, (920, 730))
        result = 'A - left'
        textsurface = myfont.render(result, False, (255, 255, 255))
        win.blit(textsurface, (920, 760))
        result = 'D - right'
        textsurface = myfont.render(result, False, (255, 255, 255))
        win.blit(textsurface, (920, 790))
        result = 'R - special ability'
        textsurface = myfont.render(result, False, (255, 255, 255))
        win.blit(textsurface, (920, 820))
        result = 'F - save game'
        textsurface = myfont.render(result, False, (255, 255, 255))
        win.blit(textsurface, (920, 850))

    def startGamePrompt(self, win):
        inputX = pygame.Rect(140, 100, 140, 32)
        inputY = pygame.Rect(140, 200, 140, 32)
        buttonEnter = pygame.Rect(60, 300, 140, 32)
        buttonLoad = pygame.Rect(300, 300, 140, 32)
        font = pygame.font.SysFont('Comic Sans MS', 16)
        clock = pygame.time.Clock()
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        colorX = color_inactive
        colorY = color_inactive
        done = False
        activeX = False
        activeY = False
        textX = ''
        textY = ''
        buttonText = 'Submit dimensions'
        buttonLoadText = 'Load game'
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if inputX.collidepoint(event.pos):
                        activeX = True
                        activeY = False
                    elif inputY.collidepoint(event.pos):
                        activeX = False
                        activeY = True
                    elif buttonEnter.collidepoint(event.pos):
                        if textX and textY:
                            return textX, textY
                    elif buttonLoad.collidepoint(event.pos):
                        self.loadGame()
                        return 0, 0
                    else:
                        activeX = False
                    colorX = color_active if activeX else color_inactive
                    colorY = color_active if activeY else color_inactive
                if event.type == pygame.KEYDOWN:
                    if activeX:
                        if event.key == pygame.K_RETURN:
                            print(textX)
                            textX = ''
                        elif event.key == pygame.K_BACKSPACE:
                            textX = textX[:-1]
                        else:
                            textX += event.unicode
                    if activeY:
                        if event.key == pygame.K_RETURN:
                            print(textY)
                            textY = ''
                        elif event.key == pygame.K_BACKSPACE:
                            textY = textY[:-1]
                        else:
                            textY += event.unicode

            bg = pygame.image.load('vworld/images/dirt.png')
            bg = pygame.transform.scale(bg, (1440, 900))
            win.blit(bg, (0, 0))

            infoSurfaceX = font.render('Width X: ', True, color_inactive)
            txt_surfaceX = font.render(textX, True, colorX)
            infoSurfaceY = font.render('Height Y: ', True, color_inactive)
            txt_surfaceY = font.render(textY, True, colorY)
            txt_surfaceButt = font.render(buttonText, True, color_inactive)
            txt_surfaceButtLoad = font.render(buttonLoadText, True, color_inactive)

            widthX = max(200, txt_surfaceX.get_width() + 10)
            widthY = max(200, txt_surfaceY.get_width() + 10)
            widthButt = max(200, txt_surfaceButt.get_width() + 10)
            widthButtLoad = max(200, txt_surfaceButtLoad.get_width() + 10)

            inputX.w = widthX
            inputY.w = widthY
            buttonEnter.w = widthButt
            buttonLoad.w = widthButtLoad

            win.blit(txt_surfaceX, (inputX.x + 5, inputX.y + 5))
            win.blit(infoSurfaceX, (inputX.x - 100, inputX.y + 5))
            win.blit(txt_surfaceY, (inputY.x + 5, inputY.y + 5))
            win.blit(infoSurfaceY, (inputY.x - 105, inputY.y + 5))
            win.blit(txt_surfaceButt, (buttonEnter.x + 5, buttonEnter.y + 5))
            win.blit(txt_surfaceButtLoad, (buttonLoad.x + 5, buttonLoad.y + 5))

            pygame.draw.rect(win, colorX, inputX, 2)
            pygame.draw.rect(win, colorY, inputY, 2)
            pygame.draw.rect(win, color_inactive, buttonEnter, 2)
            pygame.draw.rect(win, color_inactive, buttonLoad, 2)
            pygame.display.flip()
            clock.tick(30)

    def populate(self):
        availableOrganisms = [o.Antelope.Antelope, o.Belladonna.Belladonna, o.CyberSheep.CyberSheep, o.Fox.Fox,
                              o.Grass.Grass, o.Guarana.Guarana, o.Hogweed.Hogweed, o.Sheep.Sheep,
                              o.SowThistle.SowThistle, o.Turtle.Turtle, o.Wolf.Wolf]

        height = random.choice(range(self.sizeY))
        width = random.choice(range(self.sizeX))
        self.addOrganism(o.Human.Human(Position(width, height), self))
        for height in range(self.sizeY):
            for width in range(self.sizeX):
                if not random.randrange(0, 10):
                    if not self.getOrganismFromPosition(Position(width, height)):
                        self.addOrganism(random.choice(availableOrganisms)(Position(width, height), self))

    def drawWorld(self, win):
        result = f'turn: {self.turn}'
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        textsurface = myfont.render(result, False, (255, 255, 255))
        win.blit(textsurface, (920, 0))
        for height in range(self.sizeY):
            for width in range(self.sizeX):
                organism = self.getOrganismFromPosition(Position(width, height))
                if organism:
                    result += str(organism.symbol)
                    path = f'vworld/images/{self.images[organism.symbol]}.png'
                    img = pygame.image.load(path)
                    img = pygame.transform.scale(img, (900 // self.sizeX, 900 // self.sizeY))
                    win.blit(img, (width * 900 // self.sizeX, height * 900 // self.sizeY))
                else:
                    result += self.separator
                result += ' '
            result += '\n'
        return result
