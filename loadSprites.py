import pygame
import os

class loadSprites(object):
    def __init__(self):
        self.current_path = os.path.dirname(__file__)# Where your .py file is located
        self.image_path = os.path.join(self.current_path, 'images')# The image folder path for penguinRun
        self.penguinRunFolder = os.path.join(self.image_path, 'penguinRun')
        self.penguinIdleFolder = os.path.join(self.image_path, 'penguinIdle')
        self.penguinJumpFolder = os.path.join(self.image_path, 'penguinJump')
        self.penguinSlideStartFolder = os.path.join(self.image_path, 'penguinSlideStart')

        return

    def walkLeft(self):
        walkLeft = [pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunLeft_00.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunLeft_01.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunLeft_02.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunLeft_03.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunLeft_04.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunLeft_05.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunLeft_06.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunLeft_07.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunLeft_08.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunLeft_09.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunLeft_10.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunLeft_11.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunLeft_12.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunLeft_13.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunLeft_14.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunLeft_15.png'))]

        return walkLeft

    def walkRight(self):
        walkRight = [pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunRight_00.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunRight_01.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunRight_02.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunRight_03.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunRight_04.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunRight_05.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunRight_06.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunRight_07.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunRight_08.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunRight_09.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunRight_10.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunRight_11.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunRight_12.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunRight_13.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunRight_14.png')),
        pygame.image.load(os.path.join(self.penguinRunFolder, 'PenguinPistolRunRight_15.png'))]

        return walkRight
    def idleRight(self):
        idleRight = [pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_00.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_01.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_02.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_03.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_04.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_05.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_06.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_07.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_08.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_09.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_10.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_11.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_12.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_13.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_14.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_15.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_16.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_17.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_18.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_19.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_20.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_21.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_22.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_23.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_24.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_25.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_26.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_27.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_28.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_29.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_30.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_31.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_32.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_33.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_34.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_35.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_36.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_37.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_38.png')),
                          pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleRight_39.png'))]

        return idleRight

    def idleLeft(self):
        idleLeft = [pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_00.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_01.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_02.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_03.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_04.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_05.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_06.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_07.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_08.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_09.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_10.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_11.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_12.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_13.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_14.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_15.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_16.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_17.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_18.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_19.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_20.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_21.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_22.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_23.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_24.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_25.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_26.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_27.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_28.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_29.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_30.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_31.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_32.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_33.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_34.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_35.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_36.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_37.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_38.png')),
                         pygame.image.load(os.path.join(self.penguinIdleFolder, 'PenguinIdleLeft_38.png'))]
        return idleLeft

    def jumpRight(self):

        jumpRight = [pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_00.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_01.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_02.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_03.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_04.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_05.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_06.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_07.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_08.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_09.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_10.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_11.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_12.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_13.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_14.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_15.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_16.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_17.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_18.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_19.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_20.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_21.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_22.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_23.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_24.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_25.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_26.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_27.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_28.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_29.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_30.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_31.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_32.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_33.png')),
                          pygame.image.load(os.path.join(self.penguinJumpFolder, 'PenguinJumpRight_34.png'))]

        return jumpRight
    def startSlideRight(self):
        startSlideRight = [pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_00.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_01.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_02.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_03.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_04.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_05.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_06.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_07.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_08.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_09.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_10.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_11.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_12.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_13.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_14.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_15.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_16.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_17.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_18.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_19.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_20.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_21.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_22.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_23.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_24.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_25.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_26.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_27.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_28.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_29.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_30.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_31.png')),
                           pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartRight_32.png'))]
        return startSlideRight
    def startSlideLeft(self):
        startSlideLeft = [pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_00.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_01.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_02.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_03.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_04.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_05.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_06.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_07.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_08.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_09.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_10.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_11.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_12.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_13.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_14.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_15.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_16.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_17.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_18.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_19.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_20.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_21.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_22.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_23.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_24.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_25.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_26.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_27.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_28.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_29.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_30.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_31.png')),
                          pygame.image.load(os.path.join(self.penguinSlideStartFolder, 'PenguinSlideStartLeft_32.png'))]
        return startSlideLeft