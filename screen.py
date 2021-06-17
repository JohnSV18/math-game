import pygame
import random
from game import Ball

class Screen():
    """Will draw everything that should be shown on the screen."""
    def __init__(self):
        self.screen_rect = tuple(900, 600)
        self.screen = pygame.display.set_mode(self.screen_rect)
        self.black = (0, 0, 0)
        pygame.font.init()
        self.health_font = pygame.font.SysFont('comicsans', 40)
        self.frames_per_second = 60
        pygame.display.set_caption("The Sky is Falling!")
    

    def draw_window(self, basket, balls, health, points, target_score):
        self.screen.fill((255,255,255))
        self.screen.blit(basket.display_basket(), (basket.rect.x, basket.rect.y))
        target_point_text = self.health_font.render("Target Point: " + str(target_score), 1, self.black)
        self.screen.blit(target_point_text, (680, 25))
        health_text = self.health_font.render("Health: " + str(health), 1, self.black)
        self.screen.blit(health_text, (680, 50))
        score_text=self.health_font.render("Score: " + str(points), 1, self.black)
        self.screen.blit(score_text, (680, 75))

        Ball.display_balls(basket, balls)
        Screen.display_stats(points, target_score, health)
        pygame.display.update()

    def display_stats(self, points, target_score, health):

        if points == target_score:
            won_text = self.health_font.render("You Win!", 1, self.black)
            self.screen.blit(won_text, (self.screen_width/2, self.screen_height/2))
        elif health <= 0:
            lost_health_text = self.health_font.render("You Lose!", 1, self.black)
            self.screen.blit(lost_health_text, (self.screen_width/2, self.screen_height/2))