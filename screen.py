import pygame

class Screen():
    def __init__(self):
        """This class handles drawing the properties for the screen"""
        self.screen_size = (900, 600)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.black_color = (0, 0, 0)
        pygame.font.init()
        self.health_font = pygame.font.SysFont('comicsans', 25)
        self.circle_number = pygame.font.SysFont('comicsans', 16)
        self.frames_per_second = 60
        pygame.display.set_caption("The Sky is Falling!")
                
    def display_stats(self, points, target_score, health):
        """This method displays the stats of the game"""
        if points == target_score:
            won_text = self.health_font.render("You Win!", 1, self.black_color)
            self.screen.blit(won_text, (self.screen_size[0]/2, self.screen_size[1]/2))
        elif health <= 0 or points > target_score:
            lost_health_text = self.health_font.render("You Lose!", 1, self.black_color)
            restart_game_text = self.health_font.render("Press Shift To Restart", 1, self.black_color)
            self.screen.blit(lost_health_text, (self.screen_size[0]/3, self.screen_size[1]/3))
            self.screen.blit(restart_game_text, (self.screen_size[0]/3, self.screen_size[1]/2))

    def display_balls(self, balls):
        """This method displays all the occuring balls that should be displayed"""
        
        for ball in balls:
            number_in_circle = self.circle_number.render(str(ball.number), 1, self.black_color) 
            pygame.draw.circle(self.screen, ball.ball_color, (ball.rect.x + 5, ball.rect.y + 10), ball.rect.width, ball.rect.height)
            self.screen.blit(number_in_circle,(ball.rect.x, ball.rect.y))
        
    def draw_window(self, basket, balls, health, points, target_score):
        """This method draws the window of the game"""
        target_point_text = self.health_font.render("Target Point: " + str(target_score), 1, self.black_color)
        health_text = self.health_font.render("Health: " + str(health), 1, self.black_color)
        score_text=self.health_font.render("Score: " + str(points), 1, self.black_color)

        self.screen.fill((255,255,255))
        self.screen.blit(basket.display_basket(), (basket.rect.x, basket.rect.y))
        self.screen.blit(target_point_text, (680, 25))
        self.screen.blit(health_text, (680, 50))
        self.screen.blit(score_text, (680, 75))

        self.display_balls(balls)
        self.display_stats(points, target_score, health)
        pygame.display.update()

    
            