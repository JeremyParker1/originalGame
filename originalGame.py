from loadSprites import *
from character import player
import time
pygame.init()

window = pygame.display.set_mode((900,500))

screenWidth = 900
screenHeight = 500

pygame.display.set_caption("Jeremy's Game")

current_path = os.path.dirname(__file__) # Where your .py file is located
penguinRunFolder = os.path.join(current_path, 'images/penguinRun') # The image folder path for penguinRun
bg = pygame.image.load(os.path.join(penguinRunFolder, 'gameBG.png'))
clock = pygame.time.Clock()


def redrawGameWindow():
    window.blit(bg, (0, 0))
    man.draw(window)
    pygame.display.update()

crashed = False
man = player(50, 350, 64, 64)
pressed_left, pressed_right, pressed_up, pressed_down = False, False, False, False
while not crashed:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pressed_left = True
            elif event.key == pygame.K_RIGHT:
                pressed_right = True
            elif event.key == pygame.K_UP:
                pressed_up = True
            elif event.key == pygame.K_DOWN:
                pressed_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                    pressed_left = False
            elif event.key == pygame.K_RIGHT:
                    pressed_right = False
            elif event.key == pygame.K_UP:
                    pressed_up = False
            elif event.key == pygame.K_DOWN:
                    pressed_down = False
        print(event)

    keys = pygame.key.get_pressed()
    if pressed_down and not man.isJump:
        man.crouching = True
        man.standing = False
        man.isJump = False
    else:
        man.crouching = False
    if pressed_left and man.x > man.vel:
        man.x -= man.vel  # moves character left
        man.left = True
        man.right = False
        man.standing = False
    elif pressed_right and man.x < screenWidth - man.width - man.vel:
        man.x += man.vel  # moves character right
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
    if not man.isJump:
        if keys[pygame.K_UP]:
            man.isJump = True
            man.crouching = False
    else:
        if man.jumpCount >= -10:  # jC = 10, penguin goes up, jC -= until 0, penguin goes down, jC resets when <= -10
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount/1.5)**2 * neg
            man.jumpCount -= 2  # increase this number if you want to increase penguin jump duration
        else:
            man.isJump = False
            man.jumpCount = 10
    redrawGameWindow()

pygame.quit()