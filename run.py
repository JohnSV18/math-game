import pygame
import random
from screen import Screen
from ball import Ball
from basket import Basket

def main():
    """Runs the whole game and also stops it once the requirements are met"""
    target_score = random.randint(7,88)
    health = 6
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
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    target_score = random.randint(7,88)
                    health = 100
                    points = 0
                    velocity = 7
                    ball.rect.y += 3
            
                 
        while len(balls) < 4:
            ball = Ball((random.randint(0,10)))
            print(ball)
            ball.set_position_x()
            balls.append(ball)
            
        # have an array of random numbers and have the ball.rect.y choose from those
        # or having a different random speed for each ball but eventually we want more than 3 balls to start falling as well.
    
        for ball in balls:
            if health > 0 and points < target_score:
                # ball.rect.y += random.randint(2,9)           
                ball.rect.y += 3      
            else:
                ball.rect.y = -10
                velocity = 0
            if points == target_score:
                ball.rect.y = -10
                velocity = 0
                

            if ball.check_ball_collision(basket):
                points += int(ball.number)
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
