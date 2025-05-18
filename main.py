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
        self.initial_load = False
        pygame.display.set_caption("Zombie Game")

        self.clock = pygame.time.Clock()
        self.camera_pos = [0, 0]
        self.camera_movement_x = [False, False] #Left-Right
        self.camera_movement_y = [False, False] #Down-Up
        self.camera_velocity = 6


        self.MAPTILE_SIZE = 256
        self.BACKGROUND_TILE_SIZE = (self.MAPTILE_SIZE, self.MAPTILE_SIZE)
        self.BACKGROUND_COLOR = (255, 255, 255)
        self.BACKGROUND_SIZE = self.MAPTILE_SIZE ** 2

        # self.player = pygame.rect.Rect(5, 5, 1, 1)
        self.images = {
            "player" : pygame.image.load("costume2.png").convert(),
            "background_tile" : pygame.image.load("maptile.png").convert(),
            "shadow" : pygame.image.load("shadow.png"),
        }

    def update_camera(self):
        self.camera_pos[0] += (self.camera_movement_x[1] - self.camera_movement_x[0]) * self.camera_velocity
        self.camera_pos[1] += (self.camera_movement_y[1] - self.camera_movement_y[0]) * self.camera_velocity

    def load_background(self):
        for x in range(-self.BACKGROUND_SIZE, self.BACKGROUND_SIZE, self.BACKGROUND_SIZE):
            for y in range(-self.BACKGROUND_SIZE, self.BACKGROUND_SIZE, self.BACKGROUND_SIZE):
                self.screen.blit(self.images["background_tile"], (x,y))
    def main(self):
        while self.run:
            self.screen.fill(self.BACKGROUND_COLOR)
            self.clock.tick(60)
            self.load_background()

            if not self.initial_load:
                self.initial_load = True
            # self.mouse_clicked = pygame.mouse.get_pressed()
            # if self.mouse_clicked[0] == True:

            self.mouse_pos = pygame.mouse.get_pos()
            cell_size = 8
            self.shadow_pos = (((round(self.mouse_pos[0]/cell_size))*8, round(self.mouse_pos[1]/cell_size)*8))




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
            self.screen.blit(self.images["player"], (self.camera_pos[0], self.camera_pos[1]))

            pygame.display.update()


Game().main()