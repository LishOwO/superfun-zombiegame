import pygame
from math import*
import sys

pygame.init()

class Game:
    def __init__(self):
        self.SCREEN_WIDTH = 256*3
        self.SCREEN_HEIGHT = 256*3
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.run = True
        self.initial_load = False
        pygame.display.set_caption("Zombie Game")

        # self.player = pygame.rect.Rect(5, 5, 1, 1)
        self.images = {
            "player" : pygame.image.load("costume2.png").convert(),
            "background_tile" : pygame.image.load("maptile.png").convert(),
            "shadow" : pygame.image.load("shadow.png").convert(),
            "other" : pygame.image.load("other.png"),
        }

        for i in range (10):
            self.images[f"{i}"] = pygame.image.load(f"{i}.png")

        self.clock = pygame.time.Clock()
        self.camera_pos = [0, 0]
        self.camera_movement_x = [False, False] #Left-Right
        self.camera_movement_y = [False, False] #Down-Up
        self.camera_velocity = 6

        self.MAPTILE_SIZE = 256
        self.BACKGROUND_TILE_SIZE = (self.MAPTILE_SIZE, self.MAPTILE_SIZE)
        self.BACKGROUND_COLOR = (255, 255, 255)
        self.BACKGROUND_SIZE = self.MAPTILE_SIZE * 3

    def update_camera(self):
        self.camera_pos[0] += (self.camera_movement_x[1] - self.camera_movement_x[0]) * self.camera_velocity
        self.camera_pos[1] += (self.camera_movement_y[1] - self.camera_movement_y[0]) * self.camera_velocity

    def render_background(self, camera_position):
        """
        alpha_pos = (self.camera_pos[0] // self.MAPTILE_SIZE, self.camera_pos[1] // self.MAPTILE_SIZE)
        starting_pos = (alpha_pos[0]-1)+(alpha_pos[1]+1)*3 # ((x-1) + (y1) * map_width)

        for coord in range(9):
            relative_coord_x, relative_coord_y = self.map_coords[coord]
            texture_n = starting_pos + relative_coord_x + relative_coord_y * 3
            self.screen.blit(self.map[texture_n], ((self.camera_pos[0] - relative_coord_x)*self.MAPTILE_SIZE, (self.camera_pos[1] - relative_coord_y*self.MAPTILE_SIZE))) # ts renders the on-screen map tiles every 256 pixels
        """

        camera_position_x, camera_position_y = camera_position

        nearest_corner = [camera_position_x - camera_position_x % self.MAPTILE_SIZE, camera_position_y - camera_position_y % self.MAPTILE_SIZE]
        minimum_coords = [nearest_corner[0] - self.MAPTILE_SIZE, nearest_corner[1] - self.MAPTILE_SIZE]
        screens_left = [self.SCREEN_WIDTH // self.MAPTILE_SIZE, self.SCREEN_HEIGHT // self.MAPTILE_SIZE]

        max_coords_x = nearest_corner[0] + screens_left[0] * self.MAPTILE_SIZE
        max_coords_y = nearest_corner[1] + screens_left[1] * self.MAPTILE_SIZE


        for x in range(minimum_coords[0], max_coords_x+1, self.MAPTILE_SIZE):
            for y in range(minimum_coords[1], max_coords_y+1, self.MAPTILE_SIZE):
                self.screen.blit(self.images["background_tile"], (camera_position_x - x + 256*1.5, camera_position_y - y + 256*1.5))
        # + 256*1.5 des deux cotés

        # camera_position_x, camera_position_y = camera_position
        # init_alpha_pos = floor(camera_position_x/self.MAPTILE_SIZE) - floor(camera_position_y/self.MAPTILE_SIZE) * 3
        # print("camera position:", camera_position, init_alpha_pos)

        # rel_y = -(3-1)/2
        # for y in range(3):
        #     rel_x = -(3-1)/2
        #     for x in range(3):
        #         alpha_pos = round(init_alpha_pos + rel_x - rel_y* 3)
        #         x = camera_position_x-rel_x*self.MAPTILE_SIZE
        #         y = camera_position_y+rel_y*self.MAPTILE_SIZE
        #         # self.screen.blit(self.images["background_tile"], ((x%self.MAPTILE_SIZE*1.5), (y%self.MAPTILE_SIZE*1.5)))
        #         self.screen.blit(self.images["background_tile"], (-x, -y))
        #         if alpha_pos > -1 and alpha_pos < 10:
        #             self.screen.blit(self.images[str(alpha_pos)], (-x, -y))

        #         rel_x += 1
        #     rel_y -= 1


    def main(self):
        while self.run:
            self.screen.fill(self.BACKGROUND_COLOR)
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

            self.mouse_pos = pygame.mouse.get_pos()
            cell_size = 8
            self.shadow_pos = ((self.mouse_pos[0] // cell_size) * 8, (self.mouse_pos[1] // cell_size) * 8)

            # self.draw_shadow()


            self.update_camera()
            self.render_background(self.camera_pos)
            self.screen.blit(self.images["player"], (self.camera_pos[0]-256, self.camera_pos[1]-256))

            pygame.display.update()


Game().main()