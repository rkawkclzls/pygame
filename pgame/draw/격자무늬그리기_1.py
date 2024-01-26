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
        
        for i in range(4): 
            pygame.draw.line(screen, (255,0,0), (i*10,0), (i*10,30),3)
        
            pygame.draw.line(screen, (255,0,0), (0,i*10), (30,i*10),3)
        pygame.display.update()

runGame()
# pygame.quit()