from loadSprites import *
loadSprites = loadSprites()
walkLeft = loadSprites.walkLeft()
walkRight = loadSprites.walkRight()
idleRight = loadSprites.idleRight()
idleLeft = loadSprites.idleLeft()
startSlideRight = loadSprites.startSlideRight()
startSlideLeft = loadSprites.startSlideLeft()
penguinIdlePistolShootRight = loadSprites.penguinIdlePistolShootRight()
penguinIdlePistolShootLeft = loadSprites.penguinIdlePistolShootLeft()
penguinSlideShootRight = loadSprites.penguinSlidePistolShootRight()
penguinSlideShootLeft = loadSprites.penguinSlidePistolShootLeft()

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.vel = 14
        self.isJump = False
        self.jumpCount = 10
        self.idleCount = 0
        self.left = False
        self.right = False
        self.standing = True
        self.crouching = False
        self.crouchCount = 0
        self.shooting = False
        self.shootIdleCount = 0
        self.shootSlideCount = 0
    def draw(self, window): #iterates thru and resets animations. if jumping/walking, not idling.
        if self.walkCount + 1 >= 16 or self.idleCount + 1 >= 40 or self.crouchCount + 1 >= 32:
            self.walkCount = 0
            self.idleCount = 0
            self.crouchCount = 30
        if self.shootIdleCount + 1 >= 8:
            self.shootIdleCount = 0
        if self.shootSlideCount + 1 >= 8:
            self.shootSlideCount = 0
        if not self.standing and not self.crouching:  # walking left or right
            if self.left:
                window.blit(walkLeft[self.walkCount], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                window.blit(walkRight[self.walkCount], (self.x, self.y))
                self.walkCount += 1
        elif self.crouching:  # slide animations
            if self.right:
                if self.shooting:  # shooting right and crouching/sliding
                    window.blit(penguinSlideShootRight[self.shootSlideCount], (self.x - 13, self.y + 39))
                    self.shootSlideCount += 2
                else:
                    window.blit(startSlideRight[self.crouchCount], (self.x - 13, self.y - 14))
                    self.crouchCount += 5
            else:
                if self.shooting:  # shooting left and crouching/sliding
                    window.blit(penguinSlideShootLeft[self.shootSlideCount], (self.x - 39, self.y + 39))
                    self.shootSlideCount += 2
                else:
                    window.blit(startSlideLeft[self.crouchCount], (self.x - 30, self.y - 14))
                    self.crouchCount += 5
        else:  # idle animations, with stand-still shooting
            if self.right:
                if self.shooting:
                    window.blit(penguinIdlePistolShootRight[self.shootIdleCount], (self.x, self.y))
                    self.shootIdleCount += 2
                else:
                    window.blit(idleRight[self.idleCount], (self.x, self.y))
                    self.idleCount += 1
            else:
                if self.shooting:
                    window.blit(penguinIdlePistolShootLeft[self.shootIdleCount], (self.x, self.y))
                    self.shootIdleCount += 2
                else:
                    window.blit(idleLeft[self.idleCount], (self.x, self.y))
                    self.idleCount += 1
            self.crouchCount = 0
