import pygame
from global_param import *
from map import global_map

def ray_casting(root, player_pos, player_angle):
    cur_angle = player_angle - FOV/2 # Первый луч
    x0, y0 = player_pos
    for ray in range (COUNT_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range (MAX_DRAW):
            x = x0+depth * cos_a
            y = y0 + depth * sin_a
            if (x // WALL_SIZE * WALL_SIZE, y //WALL_SIZE * WALL_SIZE) in global_map:
                depth *= math.cos(player_angle - cur_angle)
                try:
                    proj_height = COEFF / depth
                except ZeroDivisionError:
                    proj_height = COEFF / 1
                c = 255/ (1 + depth * depth * 0.00001)
                pygame.draw.rect(root, (c//2,c//2,c//3), (ray * SCALE, DISPLAY_HEIGHT/2 - proj_height //2, SCALE, proj_height))
                break
        cur_angle += DELTA_ANGLE