import pygame
import random

pygame.init()

#3. pygame에 사용되는 전역변수 선언
WHITE = (255, 255, 255)
size = [400, 400]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

#4. pygame 무한루프
def runGame():
    global done
    while not done:
        clock.tick(10)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
        # where = screen, color=(0, 0, 255),
        # rect = (x,y,width,height), width = 굵기 height = 높이
        pygame.draw.rect(screen,(0, 0, 255), (0, 0, 200, 100)) 
        pygame.draw.rect(screen, (255, 0, 255), (255, 255, 255, 255))
        # circle = screen, color = (0, 0, 255), 중심좌표(x, y) = (100, 200), radius(반지름) = 30
        pygame.draw.circle(screen, (255, 0, 0), (127.5, 127.5), 30)
        pygame.draw.circle(screen, (0,255,255), (100,200),30, 1)
        pygame.draw.circle(screen, (255,0,0), (160,200), 30, 2)
        pygame.draw.circle(screen, (255, 0, 0), (220, 200), 30, 3)
        # line = screen,color =(255, 0, 0)
        # line = 시작좌표(x, y), 끝 좌표(x, y) thickqess = 굵기
        pygame.draw.line(screen, (255, 0, 0), (0, 0), (200, 200), 100)
        pygame.draw.line(screen, (255, 255, 0), (0,100), (0, 300), 5)
        pygame.draw.line(screen, (255, 0, 255), (100,300), (600,300), 5)

        pygame.display.update()

runGame()
# pygame.quit()