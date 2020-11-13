#1.게임에 필요한 모듈들

import pygame
import random as r
from datetime import datetime, timedelta
import os

#2. 게임 초기화
pygame.init()


#3. 게임에 필요한 색상 변수들
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)


#4. 게임에 들어갈 화면
size = [400,400]
screen = pygame.display.set_mode(size)

#5. 게임에 들어갈 사운드 경로
current_path = os.path.dirname(__file__)  # 경로 설정: 현재 파일의 위치 반환
sound_path = os.path.join(current_path, "game_sounds") #sounds 폴더 위치 반환



#6. 게임 시간 설정
clock = pygame.time.Clock()
last_moved_time = datetime.now()


#7. 게임에 필요한 그리기 함수
def draw_block(screen, color, position):
    block = pygame.Rect((position[0]*20,position[1]*20),(20,20))
    pygame.draw.rect(screen,color,block)


#8. 방향키 정의
key_direction = {
     pygame.K_UP : 'UP',
     pygame.K_DOWN : 'DOWN',
     pygame.K_LEFT : 'LEFT',
     pygame.K_RIGHT : 'RIGHT',}


#9. 사과 클래스
class Apple():
    def __init__(self, position=(10,10)):
        self.position = position

    def draw(self):
        draw_block(screen,red,self.position)


#10. 뱀 클래스
class Snake():
    def __init__(self):
        self.positions = [(5,5),(4,5),(3,5)]
        self.direction = ''

    def draw(self):
        for position in self.positions:
            draw_block(screen,green,position)

    def move(self):
        head_position = self.positions[0]
        x,y = head_position
        if self.direction == 'UP':
            self.positions = [(x,y-1)] + self.positions[:-1]
        elif self.direction == 'DOWN':
            self.positions = [(x,y+1)] + self.positions[:-1]
        elif self.direction == 'LEFT':
            self.positions = [(x-1,y)] + self.positions[:-1]
        elif self.direction == 'RIGHT':
            self.positions = [(x+1,y)] + self.positions[:-1]



#8. 게임 무한 루프
running = True
while running:
    dt = clock.tick(30) #게임 화면의 초당 프레임을 설정
 
    # 10 fps : 1초 동안에 10번 동작 : 1번에 10만큼 이동
    # 20 fps : 1초 동안에 20번 동작 : 1번에 5만큼 이동

    #배경화면색 설정
    screen.fill(white)

    #클래스 인스턴스화
    apple = Apple()
    snake = Snake()

    # 게임 창 닫기 이벤트
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key in key_direction:
                snake.direction = key_direction[event.key]

        if timedelta(seconds=0.1) <= datetime.now() - last_moved_time:
            snake.move()
            last_moved_time = datetime.now()




    


        # 뱀과 사과 그리기
        apple.draw()
        snake.draw()

        # 게임 업데이트
        pygame.display.update()



# 게임 종료
pygame.quit()

