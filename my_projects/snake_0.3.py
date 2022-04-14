import pygame
import math
import random
import time

pygame.init()

height = 600
width = 800

radius_snake = 15
radius_snake_tails = 10
speed_snake = 7
route_snake = 0
delta_snake = 20
center_coords = [[int((width // 2) - (delta_snake // 2)), int((height // 2) - (delta_snake // 2))]]
snake_list = center_coords.copy()

snake_list.append([400, 300])

x_delta = 0
y_delta = 0


def change_coords(snake_list_c, x_d, y_d):
    bub = []
    for i in range(len(snake_list_c)):
        if i == 0:
            x1 = snake_list_c[i][0] + x_d
            y1 = snake_list_c[i][1] + y_d
        else:
            x1 = snake_list_c[i - 1][0]
            y1 = snake_list_c[i - 1][1]
        bub.append([x1, y1])
    return bub


def food_generation(field, radius=20):
    if field == []:
        field.append([int((random.randint(1, 39) * radius) - radius / 2), int((random.randint(1, 29) * radius) - radius / 2)])
    return field


# food
very_good_food_x = int((random.randint(1, 39) * 20) - 20 / 2)
very_good_food_y = int((random.randint(1, 29) * 20) - 20 / 2)
good_food_x = int((random.randint(1, 39) * 20) - 20 / 2)
good_food_y = int((random.randint(1, 29) * 20) - 20 / 2)
bad_food_x = int((random.randint(1, 39) * 20) - 20 / 2)
bad_food_y = int((random.randint(1, 29) * 20) - 20 / 2)


def change_power(snake_list_f, changed):
    if changed == '+':
        snake_list_f.append(snake_list_f[(len(snake_list_f) - 1)])
    elif changed == '-':
        if len(snake_list_f) > 1:
            snake_list_f.pop()
        else:
            global game_over
            game_over = True


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
                if route_snake == 3:
                    continue
                else:
                    route_snake = 1
                    x_delta = (-1) * delta_snake
                    y_delta = 0
                    # Snake.change_route(Snake.route_snake, Snake.delta_snake)
            elif event.key == pygame.K_RIGHT:
                if route_snake == 1:
                    continue
                else:
                    route_snake = 3
                    x_delta = delta_snake
                    y_delta = 0
                    # Snake.change_route(Snake.route_snake, Snake.delta_snake)
            elif event.key == pygame.K_UP:
                if route_snake == 4:
                    continue
                else:
                    route_snake = 2
                    x_delta = 0
                    y_delta = (-1) * delta_snake
                    # Snake.change_route(Snake.route_snake, Snake.delta_snake)
            elif event.key == pygame.K_DOWN:
                if route_snake == 2:
                    continue
                else:
                    route_snake = 4
                    x_delta = 0
                    y_delta = delta_snake
                    # Snake.change_route(Snake.route_snake, Snake.delta_snake)
    main_display.fill((200, 255, 200))
    if len(snake_list) == 0:
        game_over = True
    elif 0 > snake_list[0][0] or snake_list[0][0] > 800 or 0 > snake_list[0][1] or snake_list[0][1] > 600:
        game_over = True
    elif len(snake_list) != 0:
        snake_list = change_coords(snake_list, x_delta, y_delta)

    pygame.draw.circle(main_display, (000, 255, 000), [very_good_food_x, very_good_food_y], radius_snake_tails, 0)
    pygame.draw.circle(main_display, (255, 255, 000), [good_food_x, good_food_y], radius_snake_tails, 0)
    pygame.draw.circle(main_display, (102, 000, 102), [bad_food_x, bad_food_y], radius_snake_tails, 0)

    for i in snake_list:
        pygame.draw.circle(main_display, (000, 000, 150), [snake_list[0][0], snake_list[0][1]], radius_snake, 0)
        pygame.draw.circle(main_display, (000, 000, 150), [i[0], i[1]], radius_snake_tails, 0)
    if snake_list[0][0] == very_good_food_x and snake_list[0][1] == very_good_food_y:
        change_power(snake_list, '+')
        change_power(snake_list, '+')
        speed_snake += 1
        very_good_food_x = int((random.randint(1, 39) * 20) - 20 / 2)
        very_good_food_y = int((random.randint(1, 29) * 20) - 20 / 2)
    if snake_list[0][0] == good_food_x and snake_list[0][1] == good_food_y:
        change_power(snake_list, '+')
        speed_snake += 0.5
        good_food_x = int((random.randint(1, 39) * 20) - 20 / 2)
        good_food_y = int((random.randint(1, 29) * 20) - 20 / 2)
    if snake_list[0][0] == bad_food_x and snake_list[0][1] == bad_food_y:
        change_power(snake_list, '-')
        speed_snake -= 0.5
        bad_food_x = int((random.randint(1, 39) * 20) - 20 / 2)
        bad_food_y = int((random.randint(1, 29) * 20) - 20 / 2)
    pygame.display.update()
    clock.tick(speed_snake)

    snake_Head = snake_list[0]
    j = 0
    for x in range(4, len(snake_list)):
        if snake_Head == snake_list[x]:
            game_over = True


pygame = quit()
quit()
