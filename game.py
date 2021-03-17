import pygame
import sys
import os
import random

# constants
screen_width, screen_height = 900, 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Mathtris")
frames_per_second = 60

basket_image = pygame.image.load(os.path.join('assets', 'cart.jpg'))
basket = pygame.transform.scale(basket_image, (55,40))
# Basket class which hold the attributes to the basket that will be grabbing the objects falling from above
class Basket():
    def __init__(self):
        self.height = 55
        self.width = 40
        self.score = 0
        self.positions = [(int(screen_height/2), int(screen_height/2))]
    
# the reset method will reset the score to 0 and also place the cart right at the center at the starting point.
    def reset(self):
        self.height = 55
        self.width = 40
        self.score = 0
        self.positions = [(int(screen_height/2), int(screen_height/2))]


def draw_window():
    screen.fill((255,255,255))
    screen.blit(basket, (300, 500))
    pygame.display.update()
    



def main():
    clock = pygame.time.Clock()
    game_is_running = True
    while game_is_running:
        clock.tick(frames_per_second)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_running = False

        screen.fill((130,67,90))
        draw_window()
          
        

if __name__ == "__main__":
    main()

# circle_size = 20

# grid_width = screen_width / circle_size
# grid_height = screen_height / circle_size

# class droplets():
#     def __init__(self):
#         self.position = (circle_size, circle_size)
#         self.color = (100, 65, ,210)
