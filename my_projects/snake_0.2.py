import pygame
import math
import random
import time

pygame.init()

height = 600
width = 800


class Snake:
    radius_snake = 15
    radius_snake_tails = 10
    speed_snake = 25
    route_snake = 0
    delta_snake = 20
    center_coords = [[(width // 2) - (delta_snake // 2), (height // 2) - (delta_snake // 2)]]
    snake_list = center_coords.copy()

    def change_route(route_snake = 0, coords=[], delta=15):
        route = [1, 2, 3, 4]
        if route_snake == route[0]:
            coords[0] += -delta
            coords[1] += 0
        elif route_snake == route[1]:
            coords[0] += 0
            coords[1] += -delta
        elif route_snake == route[2]:
            coords[0] += delta
            coords[1] += 0
        elif route_snake == route[3]:
            coords[0] += 0
            coords[1] += delta
        return coords

    def change_coords(snake_list, x_delta=0, y_delta=0):
        bub = []
        for i in range(len(snake_list)):
            if i == 0:
                x1 = snake_list[i][0] + x_delta
                y1 = snake_list[i][1] + y_delta
            else:
                x1 = snake_list[i][0]
                y1 = snake_list[i][1]
            bub.append([x1, y1])
        return bub

    def change_power(snake_list, changed):
        if changed == '+':
            snake_list.append(snake_list[(len(snake_list) - 1)])
        elif changed == '-':
            if len(snake_list) > 0:
                snake_list.pop()
            else:
                global game_over
                game_over = True

    def draw_sneak(self):
        for i in self.snake_list:
            pygame.draw.circle(main_display, (000, 000, 150), [self.snake_list[0][0], self.snake_list[0][1]], self.radius_snake, 0)
            pygame.draw.circle(main_display, (000, 000, 150), [i[0], i[1]], self.radius_snake_tails, 0)

main_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')

game_over = False
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if Snake.route_snake == 3:
                    continue
                Snake.route_snake = 1
            elif event.key == pygame.K_RIGHT:
                if Snake.route_snake == 1:
                    continue
                route_snake = 3
            elif event.key == pygame.K_UP:
                if Snake.route_snake == 4:
                    continue
                route_snake = 2
            elif event.key == pygame.K_DOWN:
                if Snake.route_snake == 2:
                    continue
                route_snake = 4
        Snake.change_route(Snake.route_snake, )
    if len(Snake.snake_list) == 0:
        game_over = True
    main_display.fill((200, 255, 200))
    Snake.draw_sneak(Snake)



    pygame.display.update()
    clock.tick(Snake.speed_snake)

pygame = quit()
quit()
