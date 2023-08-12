import sys
import os
from threading import Thread
import pygame
from pygame.locals import *
from support.color import Color as cs
from support.buttons import verticalButtonsDisplay  


# Thread apps that will allow multiple apps to be executed
class Threads(Thread):
    def __init__(self, app):
        Thread.__init__(self)
        self.app = app
    
    def run(self):
         # Starting the thread according to the app name sent
        if self.app != "server":
            os.system(f"python3 {self.app}/main.py &")
        else:
            os.system(f"python3 {self.app}/main.py")


# class that will display an front interface that will allow the user to choice what app he 
# wanna use
class FrontApp:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.buttons = ["Button 1", "Button 2", "Button 3"]
        self.active = None

    def handle_button_click(self, button):
        # Handle button click event here
        print(f"Button '{button}' clicked!")

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_ENTER:
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        mouse_pos = pygame.mouse.get_pos()
                        self.handle_button_click(self.check_button_click(mouse_pos))

            self.screen.fill(Color.black.value)
            self.draw_buttons()
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

    def check_button_click(self, mouse_pos):
        for i, button in enumerate(self.buttons):
            button_y = 200 + i * 50
            button_rect = pygame.Rect(300, button_y, 200, 40)
            if button_rect.collidepoint(mouse_pos):
                return button

        return None

    def draw_buttons(self):
        mouse_pos = pygame.mouse.get_pos()
        for i, button in enumerate(self.buttons):
            button_y = 200 + i * 50
            button_rect = pygame.Rect(300, button_y, 200, 40)

            if button_rect.collidepoint(mouse_pos):
                pygame.draw.rect(self.screen, Color.grey.value, button_rect)
                font_color = Color.white.value
            else:
                pygame.draw.rect(self.screen, Color.white.value, button_rect, 2)
                font_color = Color.white.value

            if self.active == button:
                pygame.draw.rect(self.screen, Color.green.value, button_rect)
                font_color = Color.black1.value

            button_text = self.font.render(button, True, font_color)
            button_text_rect = button_text.get_rect(center=button_rect.center)
            self.screen.blit(button_text, button_text_rect)


if __name__ == "__main__":
    app = FrontApp()
    app.run()