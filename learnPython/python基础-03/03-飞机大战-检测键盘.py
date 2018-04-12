# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import time

def main():
    screen = pygame.display.set_mode((480,852),0,32)
    background = pygame.image.load("./feiji/background.png")
    hero = pygame.image.load("./feiji/hero1.png")
    x = 200
    y = 700
    while True:
        screen.blit(background,(0,0))
        screen.blit(hero,(x,y))
		#判断是否是点击了退出按钮
        for event in pygame.event.get():
            # print(event.type)
            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    #控制飞机让其向左移动
                    x-=5
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    #控制飞机让其向右移动
                    x+=5
                elif event.key == K_SPACE:
                    print('space')

        pygame.display.update()
        time.sleep(0.02)

if __name__ == "__main__":
    main()
