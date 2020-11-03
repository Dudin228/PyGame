from global_param import *

text_wall_display = [ # W - wall, - empty
    'WWWWWWWWWWWWWWWWWWWW',
    'W-----------W------W',
    'W--W--------W------W',
    'WWWWWW------W--WWW-W',
    'W-----------W------W',
    'W---------WWWWW----W',
    'W------------------W',
    'W---------------WWWW',
    'WWW-----------W----W',
    'W-------W-----W----W',
    'W-------W----------W',
    'WWWWWWWWWWWWWWWWWWWW',
]

global_map = set() # Множество, содержащее координаты стен


for i, row in enumerate(text_wall_display):
    for j, block in enumerate(row):
        if block == "W":
            global_map.add((j*WALL_SIZE, i * WALL_SIZE)) # Заносим в множество координаты блоков, 
            # где i - номер строки, j - номер блока, WALL_SIZE - размер блока