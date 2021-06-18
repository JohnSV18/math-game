import pygame
import os

class Basket():
    def __init__(self):
        self.rect = pygame.Rect(300, 500, 55, 40)  
        
    def display_basket(self):
        """Displays basket/shopping cart that will be used to catch the balls."""
        basket_image = pygame.image.load(os.path.join('assets', 'cart.jpg')) 
        basket = pygame.transform.scale(basket_image, (55, 40))

        return basket

