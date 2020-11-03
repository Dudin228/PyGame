# global parametrs
import math

# colors
BLACK = (0,0,0)
WHITE = (255,255,255)
DARKBLUE = (72, 61, 139)
PEACH = (255, 218, 185)

# display
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
DELAY = 31 # Ограничение кадров в секунду

# player
player_position = (DISPLAY_WIDTH//2, DISPLAY_HEIGHT//2) # Начальная позиция игрока
player_view_angle = 0 # Начальное направление камеры
player_speed = 2

# map
WALL_SIZE = 40 # Размер блока (px)

# render settings
FOV = math.pi/2 # Угол обзора
COUNT_RAYS = 160 # Количество лучей
MAX_DRAW = 480 # Максимальная дальность прорисовки
DELTA_ANGLE = FOV / COUNT_RAYS # Угол между лучами
DIST = COUNT_RAYS / (2*math.tan(FOV/2))
COEFF = 4 * DIST * WALL_SIZE
SCALE = DISPLAY_WIDTH // COUNT_RAYS

