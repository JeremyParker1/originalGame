from loadSprites import *
loadSprites = loadSprites()
walkLeft = loadSprites.walkLeft()
walkRight = loadSprites.walkRight()
idleRight = loadSprites.idleRight()
idleLeft = loadSprites.idleLeft()
startSlideRight = loadSprites.startSlideRight()
startSlideLeft = loadSprites.startSlideLeft()
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
        self.idlePictures = 0
        self.left = False
        self.right = False
        self.standing = True
        self.crouching = False
        self.crouchCount = 0
    def draw(self, window): #iterates thru and resets animations. if jumping/walking, not idling.
        if self.walkCount + 1 >= 16 or self.idlePictures + 1 >= 40 or self.crouchCount + 1 >= 32:
            self.walkCount = 0
            self.idlePictures = 0
            self.crouchCount = 31
        if not self.standing and not self.crouching:  # walking left or right
            if self.left:
                window.blit(walkLeft[self.walkCount], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                window.blit(walkRight[self.walkCount], (self.x, self.y))
                print(self.walkCount)
                # TODO: figure out walkcount glitch
                # TODO: reorganize code, and add projectiles
                self.walkCount += 1
        elif self.crouching:  # slide animations
            if self.right:
                window.blit(startSlideRight[self.crouchCount], (self.x - 13, self.y - 14))
                self.crouchCount += 5
            else:
                window.blit(startSlideLeft[self.crouchCount], (self.x - 30, self.y - 14))
                self.crouchCount += 5
        else:  # idle animations
            if self.right:
                window.blit(idleRight[self.idlePictures], (self.x, self.y))
                self.idlePictures += 1
            else:
                window.blit(idleLeft[self.idlePictures], (self.x, self.y))
                self.idlePictures += 1
            self.crouchCount = 0
