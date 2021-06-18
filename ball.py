import pygame
import sys
import os
import random

class Ball():
    def __init__(self, number):
        self.number = number
        self.rect = pygame.Rect(0, 40, 10, 10)  
        self.ball_color = (random.randint(0,150),random.randint(100, 200), 0)

    def __repr__(self):
        return f"Ball object: {self.number}"

    def set_position_x(self):
        """Sets x-coordinate position at random ranging from 100 to 900"""
        self.rect.x = random.randint(100, 900)

    def check_ball_collision(self, basket):
        if pygame.Rect.colliderect(basket.rect, self.rect):
            # points += 1
            # balls.remove(ball)
            return True
        else:
            return False 
            # print(f"ball number {ball.number} position {ball.rect.x}")
        if ball.rect.y > screen.screen_size[1]:
            health -= 1                
            balls.remove(ball)
