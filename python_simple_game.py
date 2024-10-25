import pygame
import sys
import time

# 初期化
pygame.init()

# 画面の大きさ
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ボールバウンス")

ball_radius = 10
ball_speed_x = 5
ball_speed_y = 5
ball = pygame.Rect(screen_width // 2-ball_radius, screen_height//2-ball_radius, ball_radius*2, ball_radius*2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.display.update()