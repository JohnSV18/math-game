import pygame
import random
from screen import Screen
from ball import Ball
from basket import Basket

def main():
    """Runs the whole game and also stops it once the requirements are met"""
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
        clock.tick(screen.frames_per_second)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_running = False
                 
        while len(balls) < 3:
            ball = Ball(balls.count)
            ball.set_position_x()
            balls.append(ball)
    
        for ball in balls:
            if health > 0:
                ball.rect.y += random.randint(2,6)                
            else:
                ball.rect.y = -10
            if points == target_score:
                ball.rect.y = -10

            if ball.check_ball_collision(basket):
                points += 1
                balls.remove(ball)

            if ball.rect.y > screen.screen_size[1]:
                health -= 1                
                balls.remove(ball)

                
        # This allows the cart to move from left to right based on the keys the user is pressing
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and basket.rect.x - velocity >0:
            basket.rect.x -= velocity
        
        if keys_pressed[pygame.K_RIGHT] and basket.rect.x + velocity + basket.rect.width < screen.screen_size[0]:
            basket.rect.x += velocity

        screen.draw_window(basket, balls, health, points, target_score)
        

if __name__ == "__main__":
    main()
