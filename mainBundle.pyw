import pygame
from global_param import *
from player import Player
import math
from map import global_map
from ray_casting import ray_casting


pygame.init() # инициализация модуля

root = pygame.display.set_mode(( DISPLAY_WIDTH, DISPLAY_HEIGHT )) # создание окна

fps = pygame.time.Clock() # Кадры в секунду

cur_player = Player() # Создаем экземпляр игрока


font = pygame.font.SysFont('Arial',25, bold = True)

while True: # основной цикл
    for event in pygame.event.get(): # перебор событый, получаемых из pygame
        if event.type == pygame.QUIT: # если окно закрыто
            exit() # завершить программу
    root.fill(BLACK) # закрашивание поверхности черным цветом
    pygame.draw.rect (root, (105, 220, 255), (0,0, DISPLAY_WIDTH, DISPLAY_HEIGHT/2)) # Небо 
    pygame.draw.rect (root, (70,70,70), (0,DISPLAY_HEIGHT/2, DISPLAY_WIDTH, DISPLAY_HEIGHT/2)) # Земля
    ray_casting(root, cur_player.get_coords, cur_player.angle)
    cur_player.movement() # вызываем обработчик перемещения
    pygame.draw.rect (root, BLACK, (0,0, 400, 240)) # Фон карты
    # minimap
    pygame.draw.circle(root, WHITE, (int(cur_player.x/2), int(cur_player.y/2)), 7) # отрисовываем игрока
    pygame.draw.line(root, PEACH, (cur_player.x//2, cur_player.y//2), (cur_player.x//2 + DISPLAY_WIDTH//2 * math.cos (cur_player.angle-45)//16,
    cur_player.y//2 + DISPLAY_WIDTH//2 * math.sin(cur_player.angle-45)//16)) # рисуем линию обзора
    pygame.draw.line(root, PEACH, (cur_player.x//2, cur_player.y//2), (cur_player.x//2 + DISPLAY_WIDTH//2 * math.cos (cur_player.angle+45)//16,
    cur_player.y//2 + DISPLAY_WIDTH//2 * math.sin(cur_player.angle+45)//16)) # рисуем линию обзора
    for x,y in global_map: # проходим по множеству
       pygame.draw.rect (root, WHITE, (int(x/2),int(y/2),WALL_SIZE//2,WALL_SIZE//2)) # рисуем блоки по координатам
    # /minimap
    render = font.render(str(int(fps.get_fps()))+' fps',0,(3, 115, 7))
    root.blit(render, (DISPLAY_WIDTH - 80,10))
    pygame.display.flip() # обновление содержимого окна
    fps.tick(DELAY) # обновление счетчика времени