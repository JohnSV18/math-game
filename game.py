import pygame
import sys
import os
import random
# from screen import Screen

# pygame.font.init()
# constants
# screen_width, screen_height = 900, 600
# screen = pygame.display.set_mode((screen_width,screen_height))


# This is the speed that will be used for the basket to move from side to side.
# velocity = 7
# # The color of the balls falling from above at different random colors.
# ball_color = (random.randint(0,150),random.randint(100, 200), 0)
# Back color RBG format

# font size and style

# image of basket 




class Ball():
    def __init__(self, number):
        self.ball_color = (random.randint(0,150),random.randint(100, 200), 0)
        self.width = 10
        self.height = 10
        self.position_y = 40
        self.position_x = 0
        # using this to rep given number for the ball
        self.number = number
        self.ball_color = (random.randint(0,150),random.randint(100, 200), 0)

    def __repr__(self):
        return f"Ball object: {self.number}"


    def set_position_x(self):
        """Sets x-coordinate position at random ranging from 100 to 900"""
        self.position_x = random.randint(100, 900)

    def display_balls(self, balls):
        
        for ball in balls:
            pygame.draw.circle(self.screen, ball.ball_color, (ball.position_x, ball.position_y), ball.width, ball.height)
            if ball.position_y > self.screen_height:
                pygame.draw.circle(self.screen, ball.ball_color, (ball.position_x, ball.position_y), ball.width, ball.height)
    



class Basket():
    def __init__(self):
        self.rect = pygame.Rect(300, 500, 55, 40)  
        


    def display_basket(self):
        """Displays basket/shopping cart that will be used to catch the balls."""
        basket_image = pygame.image.load(os.path.join('assets', 'cart.jpg')) 
        basket = pygame.transform.scale(basket_image, (55, 40))

        return basket

# class Screen():
#     """Will draw everything that should be shown on the screen."""
#     def draw_window(basket, balls, health, points, target_score):

#         screen.fill((255,255,255))
#         screen.blit(basket.display_basket(), (basket.rect.x, basket.rect.y))
#         target_point_text = health_font.render("Target Point: " + str(target_score), 1, black)
#         screen.blit(target_point_text, (680, 25))
#         health_text = health_font.render("Health: " + str(health), 1, black)
#         screen.blit(health_text, (680, 50))
#         score_text=health_font.render("Score: " + str(points), 1, black)
#         screen.blit(score_text, (680, 75))

#         Ball.display_balls(basket, balls)
#         Screen.display_stats(points, target_score, health)
#         pygame.display.update()

    # def display_stats(points, target_score, health):

    #     if points == target_score:
    #         won_text = health_font.render("You Win!", 1, black)
    #         screen.blit(won_text, (screen_width/2, screen_height/2))
    #     elif health <= 0:
    #         lost_health_text = health_font.render("You Lose!", 1, black)
    #         screen.blit(lost_health_text, (screen_width/2, screen_height/2))

    



# def main():
#     target_score = random.randint(7,11)
#     health = 10
#     points = 0
#     basket = Basket()
#     clock = pygame.time.Clock()
#     game_is_running = True
#     balls = []

#     while game_is_running:
#         clock.tick(frames_per_second)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_is_running = False
                 
#         while len(balls) < 3:
#             ball = Ball(balls.count)
#             ball.set_position_x()
#             balls.append(ball)
    
#         for ball in balls:
#             if health > 0:
#                 ball.position_y += random.randint(2,6)
#             else:
#                 ball.position_y = -10
#             if points == target_score:
#                 ball.position_y = -10
                

#             ball_tuple = (ball.position_x, ball.position_y, ball.width, ball.height)

#             # checking collision 

#             if pygame.Rect.colliderect(basket.rect, ball_tuple):
#                 points += 1
#                 balls.remove(ball)
#                 print(f"ball number {ball.number} position {ball.position_x}")
#             else:
#                 print('******Balls that did not collide ******\n')
#                 print(f"ball number {ball.number} position {ball.position_x}")
#             if ball.position_y > screen_height:
#                 health -= 1                
#                 balls.remove(ball)


#         keys_pressed = pygame.key.get_pressed()
#         if keys_pressed[pygame.K_LEFT] and basket.rect.x - velocity >0:
#             basket.rect.x -= velocity
#         if keys_pressed[pygame.K_RIGHT] and basket.rect.x + velocity + basket.rect.width < screen_width:
#             basket.rect.x += velocity

#         Screen.draw_window(basket, balls, health, points, target_score)
        
        
          
        

# if __name__ == "__main__":
#     main()
