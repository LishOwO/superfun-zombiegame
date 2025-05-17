from operator import truediv

import pygame
from math import*
import sys

pygame.init()

class Game:
    def __init__(self):
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.run = True
        pygame.display.set_caption("Zombie Game")

        self.clock = pygame.time.Clock()
        self.camera_pos = [0, 0]
        self.camera_movement_x = [False, False] #Left-Right
        self.camera_movement_y = [False, False] #Down-Up
        self.camera_velocity = 3

        # self.player = pygame.rect.Rect(5, 5, 1, 1)
        self.player = pygame.image.load("costume2.png").convert()

    def update_camera(self):
        self.camera_pos[0] += (self.camera_movement_x[1] - self.camera_movement_x[0]) * self.camera_velocity
        self.camera_pos[1] += (self.camera_movement_y[1] - self.camera_movement_y[0]) * self.camera_velocity

    def main(self):
        while self.run:
            self.screen.fill((0,0,0))
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.camera_movement_x[0] = True
                    if event.key == pygame.K_LEFT:
                        self.camera_movement_x[1] = True
                    if event.key == pygame.K_DOWN:
                        self.camera_movement_y[0] = True
                    if event.key == pygame.K_UP:
                        self.camera_movement_y[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.camera_movement_x[0] = False
                    if event.key == pygame.K_LEFT:
                        self.camera_movement_x[1] = False
                    if event.key == pygame.K_DOWN:
                        self.camera_movement_y[0] = False
                    if event.key == pygame.K_UP:
                        self.camera_movement_y[1] = False
            self.update_camera()
            self.screen.blit(self.player, (self.camera_pos[0], self.camera_pos[1]))

            pygame.display.update()


Game().main()