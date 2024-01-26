import pygame
import random

pygame.init()

# 3. pygame에 사용되는 전역변수
WHITE = (255, 255, 255)
size = [400, 300]
screen = pygame.time.Clock()

# pygame에 사용하도록 비행기 이미지를 호출
airplane = pygame.image.load('images/plane.png')
airplane = pygame.transform.scale(airplane, (60, 45))
