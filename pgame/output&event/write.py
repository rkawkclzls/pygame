import pygame # 1. pygame 선언
import random

pygame.init() # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언

WHITE = (255, 255, 255)
size = [400, 400]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

# 4. pygame 무한루프
def runGame():
    global done
    while not done:
        clock.tick(10)
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True

        sysfont = pygame.font.SysFont('malgungothic', 72)
        text = sysfont.render("안녕!", True, (0,0,255))
        screen.blit(text, (0,0))
        
        pygame.display.update()

runGame()
pygame.quit()