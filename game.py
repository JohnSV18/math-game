import pygame
import sys
import os
import random
pygame.font.init()
# constants
screen_width, screen_height = 900, 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Mathtris")
frames_per_second = 60
velocity = 5
ball_color = (random.randint(0,150),random.randint(100, 200), 0)


black = (0, 0, 0)

health_font = pygame.font.SysFont('comicsans', 40)

basket_image = pygame.image.load(os.path.join('assets', 'cart.jpg'))
# basket = pygame.transform.scale(basket_image, (55,40))
# Basket class which hold the attributes to the basket that will be grabbing the objects falling from above


class Ball():
    def __init__(self, number):
        self.ball_color = (random.randint(0,150),random.randint(100, 200), 0)
        self.width = 10
        self.height = 10
        self.position_y = 40
        self.position_x = 0
        self.number = number

    def set_position_x(self):
        self.position_x = random.randint(100, 900)
    
    # def handle_balls(self):
    #     for ball in balls:
    #         if ball.colliderect(circle_basket):
    #             balls.remove(ball)
            


class Basket():
    def __init__(self):
        self.height = 55
        self.width = 40
        self.score = 0
        self.positions = [(int(screen_height/2), int(screen_height/2))]
    
# the reset method will reset the score to 0 and also place the cart right at the center at the starting points

    def show_basket(self):
        basket_image = pygame.image.load(os.path.join('assets', 'cart.jpg'))
        basket = pygame.transform.scale(basket_image, (self.height, self.width))

        return basket


def draw_window(circle_basket, x, y, balls, health, points, target_score):
    b = Basket()
    screen.fill((255,255,255))
    screen.blit(b.show_basket(), (x, y))
    health_text = health_font.render("Health: " + str(health), 1, black)
    screen.blit(health_text, )


    for ball in balls:
        pygame.draw.circle(screen, ball.ball_color, (ball.position_x, ball.position_y), ball.width, ball.height)
        if ball.position_y > screen_height:
            pygame.draw.circle(screen, ball.ball_color, (ball.position_x, ball.position_y), ball.width, ball.height)


    pygame.display.update()
    



def main():
    target_score = random.randint(7,17)
    health = 10
    points = 0
    b = Basket()
    x = 300 
    y = 500
    circle_basket = pygame.Rect(300, 500, b.height, b.width)
    clock = pygame.time.Clock()
    game_is_running = True
    balls = []
    
    circle_y_position = 40
    while game_is_running:
        clock.tick(frames_per_second)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_running = False
           
        if health <= 0:
            win_text = "You Lose!"
        if points == target_score:
            win_text = "You Win!"
        elif points > target_score:
            win_text = "You Lose!"
            
        

        while len(balls) < 4:
            ball = Ball(balls.count)
            ball.set_position_x()
            balls.append(ball)
        

    
        for ball in balls:
            ball.position_y += random.randint(2,6)

            ball_tuple = (ball.position_x, ball.position_y, ball.width, ball.height)
            print(f"ball number {ball.number} position {ball.position_x}")

            if pygame.Rect.colliderect(circle_basket, ball_tuple):
                points += 1
                balls.remove(ball)
            if ball.position_y > screen_height:
                health -= 1                
                balls.remove(ball)

                



        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and x - velocity >0:
            x -= velocity
        if keys_pressed[pygame.K_RIGHT] and x + velocity + circle_basket.width < screen_width:
            x += velocity

        draw_window(circle_basket, x, y, balls, health, points, target_score)
        
        
          
        

if __name__ == "__main__":
    main()
