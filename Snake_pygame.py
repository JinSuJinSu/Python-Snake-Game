import pygame
import os
import random as r


pygame.init()



# 화면 크기 설정
screen_width = 680
screen_height = 680


# 사과 크기 설정
apple = 40


# 뱀 크기 설정(계속 크기를 늘려야 하기 때문에 배열 형태로 만들어준다)
snake = [40,40]


screen = pygame.display.set_mode((screen_width, screen_height))

#RGB 색상 정의해준다.
white = (255, 255, 255)
blue = (0,0,255)
red = (255,0,0)


#화면을 그려준다
rect1  = pygame.Rect((0, 0), (screen_width, screen_height))
pygame.draw.rect(screen, white, rect1 )

#뱀을 그려준다(위치는 랜덤한 위치에서)
rect2  = pygame.Rect((r.randint(0, screen_width - snake[0]), r.randint(0, screen_height - snake[1])), (snake[0], snake[1]))
pygame.draw.rect(screen, blue, rect2 )

#사과를 그려준다.(위치는 랜덤한 위치에서)
rect3  = pygame.Rect((r.randint(0, screen_width - apple), r.randint(0, screen_height - apple)), (apple,apple))
pygame.draw.rect(screen, red, rect3 )



#화면 타이틀 설정
pygame.display.set_caption("snake game")


#FPS 설정
clock = pygame.time.Clock()


#파일 경로 설정
current_path = os.path.dirname(__file__)  #현재 파일의 위치 반환
sound_path = os.path.join(current_path, "game_sounds") #sounds 폴더 위치 반환



# 폰트 정의
game_font = pygame.font.Font(None, 60)

# 게임 오버 메시지
game_result = "Game over"


speed = 2


# 게임 작동을 위한 코드(기본 공식이라 생각하면 된다.)
running = True
while running:
    dt = clock.tick(30) #게임 화면의 초당 프레임을 설정

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #뱀의 움직임을 처리한다.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake[0] +=speed
            elif event.key == pygame.K_LEFT:
                snake[0] -=speed
            elif event.key == pygame.K_UP:
                snake[1] -=speed
            elif event.key == pygame.K_DOWN:
                snake[1] +=speed


    # 게임 업데이트
    pygame.display.update()




pygame.time.delay(2000)
# 게임 종료
pygame.quit()

