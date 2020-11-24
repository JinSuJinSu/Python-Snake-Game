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

#5. 게임 사운드 설정
current_path = os.path.dirname(__file__)  # 경로 설정: 현재 파일의 위치 반환
sound_path = os.path.join(current_path, "game_sounds") #sounds 폴더 위치 반환


movement_sound = pygame.mixer.Sound(os.path.join(sound_path, "movement.wav"))
death_sound = pygame.mixer.Sound(os.path.join(sound_path, "death.mp3"))
eating_sound = pygame.mixer.Sound(os.path.join(sound_path, "eating.wav"))



#6. 게임 시간 설정
clock = pygame.time.Clock()
last_moved_time = datetime.now()


#7. 뱀 방향키 설정
key_direction = {
    pygame.K_UP: 'UP',
    pygame.K_DOWN: 'DOWN',
    pygame.K_LEFT: 'LEFT',
    pygame.K_RIGHT: 'RIGHT'
}


#8. 게임에 필요한 그리기 함수
def draw_block(screen, color, position):
    block = pygame.Rect((position[0] * 20, position[1] * 20),
                        (20, 20))
    pygame.draw.rect(screen, color, block)



#9. 사과 클래스 만들기
class Apple:
    def __init__(self, position=(5, 5)):
        self.position = position
 
    def draw(self):
        draw_block(screen, red, self.position)



#10. 뱀 클래스 만들기
class Snake:
    def __init__(self):
        self.positions = [(10,10),(9,10),(8,10)]  # 뱀의 위치
        self.direction = ''
 
    def draw(self):
        for position in self.positions: 
            draw_block(screen, green, position)

    def move(self):
        head_position = self.positions[0]
        x, y = head_position
        if self.direction == 'UP':
            self.positions = [(x, y-1)] + self.positions[:-1]
        elif self.direction == 'DOWN':
            self.positions = [(x, y+1)] + self.positions[:-1]
        elif self.direction == 'LEFT':
            self.positions = [(x-1, y)] + self.positions[:-1]
        elif self.direction == 'RIGHT':
            self.positions = [(x+1, y)] + self.positions[:-1]

    def grow(self):
        tail_position = self.positions[-1]
        x, y = tail_position
        if self.direction == 'UP':
            self.positions.append((x, y-1))
        elif self.direction == 'DOWN':
            self.positions.append((x, y+1))
        elif self.direction == 'LEFT':
            self.positions.append((x-1, y))
        elif self.direction == 'RIGHT':
            self.positions.append((x+1, y))


#11. 사과, 뱀 인스턴스
apple = Apple()
snake = Snake()


#12. 점수 만들기
score = 0

#13. 게임 오버 메시지
game_result = 'Game Over'


#14. 게임 폰트 정의
game_font = pygame.font.Font(None, 60)


#15. 게임 무한루프
running = True
while running:
    clock.tick(20)
    screen.fill(white)
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: # 뱀 방향키에 따른 움직임을 반영한다.
                if event.key in key_direction:
                    snake.direction = key_direction[event.key]
                    movement_sound.play()
 
    if timedelta(seconds=0.1) <= datetime.now() - last_moved_time:
        snake.move()
        last_moved_time = datetime.now()

    # 뱀이 사과를 먹으면 길이를 증가시키고 사과 다시 생성
    if snake.positions[0] == apple.position:
        snake.grow()
        eating_sound.play()
        apple.position = (r.randint(0,19),r.randint(0,19))
        score +=1



    # 게임 오버 조건
    x_position, y_position = snake.positions[0]


    if x_position<0 or x_position>19 or y_position<0 or y_position>19 or snake.positions[0] in snake.positions[1:]:
        death_sound.play()
        running = False


 
    apple.draw()
    snake.draw()

    #점수 화면에 표시
    result_score = game_font.render(str(score), True, (0, 0, 0))
    screen.blit(result_score, (200,20))



    pygame.display.update()


#게임 오버 메시지
msg = game_font.render(game_result, True, (0, 0, 0))
msg_rect = msg.get_rect(center=(200,200))
screen.blit(msg,msg_rect)
pygame.display.update()


pygame.time.delay(2000)


# 16. 게임 종료
pygame.quit()

