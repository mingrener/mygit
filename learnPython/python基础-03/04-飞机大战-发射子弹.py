# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import time
class HeroPlane():
    def __init__(self):
        self.x = 200
        self.y = 700
        self.image = pygame.image.load("./feiji/hero1.png")
        self.bullet_list = []
    def move_left(self):
        self.x -= 10
    def move_right(self):
        self.x += 10
    def display(self,screen):
        screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.move()
            bullet.display(screen)
    def fashe_bullet(self):
        new_bullet = Bullet(self.x,self.y)
        self.bullet_list.append(new_bullet)

class Bullet():
    def __init__(self,x,y):
        self.x = x+40
        self.y = y-20
        self.image = pygame.image.load("./feiji/bullet-3.gif")
    def move(self):
        self.y -= 10
    def display(self,screen):
        screen.blit(self.image,(self.x,self.y))

def main():
    screen = pygame.display.set_mode((480,852),0,32)
    background = pygame.image.load("./feiji/background.png")
    hero = HeroPlane()
    
    while True:
        screen.blit(background,(0,0))
        hero.display(screen)
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
                    hero.move_left()
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    #控制飞机让其向右移动
                    hero.move_right()
                elif event.key == K_SPACE:
                    print('space')
                    hero.fashe_bullet()

        pygame.display.update()
        time.sleep(0.02)

if __name__ == "__main__":
    main()
