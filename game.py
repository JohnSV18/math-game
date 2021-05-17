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
# velocity of basket moving side to side
velocity = 7
# color of balls that fall from above
ball_color = (random.randint(0,150),random.randint(100, 200), 0)

black = (0, 0, 0)
# font size and style
health_font = pygame.font.SysFont('comicsans', 40)
# image of basket 
basket_image = pygame.image.load(os.path.join('assets', 'cart.jpg'))



class Ball():
    def __init__(self, number):
        self.ball_color = (random.randint(0,150),random.randint(100, 200), 0)
        self.width = 10
        self.height = 10
        self.position_y = 40
        self.position_x = 0
        # using this to rep given number for the ball
        self.number = number

    def __repr__(self):
        return f"Ball object: {self.number}"


    def set_position_x(self):
        self.position_x = random.randint(100, 900)



class Basket():
    def __init__(self):
        self.rect = pygame.Rect(300, 500, 55, 40)   


    def show_basket(self):
        basket_image = pygame.image.load(os.path.join('assets', 'cart.jpg'))
        basket = pygame.transform.scale(basket_image, (55, 40))

        return basket


def draw_window(basket, balls, health, points, target_score):
    screen.fill((255,255,255))
    screen.blit(basket.show_basket(), (basket.rect.x, basket.rect.y))
    target_point_text = health_font.render("Target Point: " + str(target_score), 1, black)
    screen.blit(target_point_text, (680, 25))
    health_text = health_font.render("Health: " + str(health), 1, black)
    screen.blit(health_text, (680, 50))
    score_text=health_font.render("Score: " + str(points), 1, black)
    screen.blit(score_text, (680, 75))



    for ball in balls:
        pygame.draw.circle(screen, ball.ball_color, (ball.position_x, ball.position_y), ball.width, ball.height)
        if ball.position_y > screen_height:
            pygame.draw.circle(screen, ball.ball_color, (ball.position_x, ball.position_y), ball.width, ball.height)
    if points == target_score:
        won_text = health_font.render("You Win!", 1, black)
        screen.blit(won_text, (screen_width/2, screen_height/2))
    elif health <= 0:
        lost_health_text = health_font.render("You Lose!", 1, black)
        screen.blit(lost_health_text, (screen_width/2, screen_height/2))
    

    pygame.display.update()
    



def main():
    target_score = random.randint(7,11)
    health = 10
    points = 0
    basket = Basket()
    clock = pygame.time.Clock()
    game_is_running = True
    balls = []

    while game_is_running:
        clock.tick(frames_per_second)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_running = False
           
        # if health <= 0:
        #     for ball in balls:
        #         ball.position_y = 0
        #     win_text = "You Lose!"
        #     print(win_text)
        # if points == target_score:
        #     win_text = "You Win!"
        #     print(win_text)
      
        while len(balls) < 3:
            ball = Ball()
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

            

            if pygame.Rect.colliderect(basket.rect, ball_tuple):
                points += 1
                balls.remove(ball)
                print(f"ball number {ball.number} position {ball.position_x}")
            else:
                print('******Balls that did not collide ******\n')
                print(f"ball number {ball.number} position {ball.position_x}")
            if ball.position_y > screen_height:
                health -= 1                
                balls.remove(ball)


        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and basket.rect.x - velocity >0:
            basket.rect.x -= velocity
        if keys_pressed[pygame.K_RIGHT] and basket.rect.x + velocity + basket.rect.width < screen_width:
            basket.rect.x += velocity

        draw_window(basket, balls, health, points, target_score)
        
        
          
        

if __name__ == "__main__":
    main()
