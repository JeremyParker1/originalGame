from loadSprites import *
from character import player
from penguinProjectile import projectile
pygame.init()

window = pygame.display.set_mode((900,500))

screenWidth = 900
screenHeight = 500

pygame.display.set_caption("Jeremy's Game")

current_path = os.path.dirname(__file__) # Where your .py file is located
images = os.path.join(current_path, 'images') # The image folder path for penguinRun
bg = pygame.image.load(os.path.join(images, 'gameBG.png'))
clock = pygame.time.Clock()


def redrawGameWindow():  # draws the animations and images to the screen
    window.blit(bg, (0, 0))
    man.draw(window)
    for bullet in bullets:
        bullet.draw(window)
    pygame.display.update()

shootLoop = 0
bullets = []
man = player(50, 350, 85, 100)
pressed_left, pressed_right, pressed_up, pressed_down = False, False, False, False
crashed = False

while not crashed:
    clock.tick(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.KEYDOWN:  # detects when an arrow key is pressed down
            if event.key == pygame.K_LEFT:
                pressed_left = True
            elif event.key == pygame.K_RIGHT:
                pressed_right = True
            elif event.key == pygame.K_UP:
                pressed_up = True
            elif event.key == pygame.K_DOWN:
                pressed_down = True
        elif event.type == pygame.KEYUP:  # detects when an arrow key is no longer pressed down
            if event.key == pygame.K_LEFT:
                    pressed_left = False
            elif event.key == pygame.K_RIGHT:
                    pressed_right = False
            elif event.key == pygame.K_UP:
                    pressed_up = False
            elif event.key == pygame.K_DOWN:
                    pressed_down = False
        print(event)

    for bullet in bullets:
        if bullet.x < 900 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 6:
        man.shooting = False
        shootLoop = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and shootLoop == 0:
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 8:
            if not man.crouching:
                man.shooting = True
                bullets.append(projectile(round(man.x + man.width), round(man.y + 50), facing))
            else:
                bullets.append(projectile(round(man.x + man.width), round(man.y + 80), facing))
            shootLoop = 1
    if pressed_down and not man.isJump:  # allows crouching if character is not jumping
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
    if not man.isJump:  # logic for jump animation
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