import pygame
import sys
import os
import random
from screen import Screen
from game import Ball, Basket

def main():
    target_score = random.randint(7,11)
    health = 10
    points = 0
    velocity = 7
    screen = Screen()
    basket = Basket()
    clock = pygame.time.Clock()
    game_is_running = True
    balls = []

    while game_is_running:
        clock.tick(Screen.frames_per_second)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_running = False
                 
        while len(balls) < 3:
            ball = Ball(balls.count)
            ball.set_position_x()
            balls.append(ball)
    
        for ball in balls:
            if health > 0:
                ball.position_y += random.randint(2,6)
            else:
                ball.position_y = -10
            if points == target_score:
                ball.position_y = -10
                

            ball_tuple = (ball.position_x, ball.position_y, ball.width, ball.height)

            # checking collision 

            if pygame.Rect.colliderect(basket.rect, ball_tuple):
                points += 1
                balls.remove(ball)
                print(f"ball number {ball.number} position {ball.position_x}")
            else:
                print('******Balls that did not collide ******\n')
                print(f"ball number {ball.number} position {ball.position_x}")
            if ball.position_y > Screen.screen_height:
                health -= 1                
                balls.remove(ball)


        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and basket.rect.x - velocity >0:
            basket.rect.x -= velocity
        if keys_pressed[pygame.K_RIGHT] and basket.rect.x + velocity + basket.rect.width < screen.screen_width:
            basket.rect.x += velocity

        screen.draw_window(basket, balls, health, points, target_score)
        
        
          
        

if __name__ == "__main__":
    main()
