import pygame
from support.color import Color

# Class that controls the initial panel
class Start:
    pygame.init()

    def __init__(self, screen, screen_size):
        self.font = pygame.font.SysFont("arial", 50)
        self.font1 = pygame.font.SysFont("arial", 12)
        self.screen = screen
        self.screen_size = screen_size
        self.delay = self.highCircle = self.count = 0

    # Method that controls this class
    def run(self, events, id):
        del events
        del id
        # Drawing title
        size = pygame.font.Font.size(self.font, 'Voterpy')
        line = self.font.render('Voterpy', True, Color.white3.value)
        self.screen.blit(line, (self.screen_size[0] / 2 - size[0] / 2, self.screen_size[1] / 2 - size[1] / 2 - 40))
        # Drawing sub-title
        size = pygame.font.Font.size(self.font1, 'Voter App')
        line = self.font1.render('Voter App', True, Color.white.value)
        self.screen.blit(line, (self.screen_size[0] / 2 - size[0] / 2, self.screen_size[1] / 2 - size[1] / 2 - 10))

        # Decrement the font1 size
        self.font1 = pygame.font.SysFont("arial", 9)

        # Drawing bottom info title
        size = pygame.font.Font.size(self.font1, 'Made by Roberto Medina')
        line = self.font1.render('Made by Roberto Medina', True, Color.white.value)
        self.screen.blit(line, (self.screen_size[0] / 2 - size[0] / 2, 430))
        # Drawing contact info title
        size = pygame.font.Font.size(self.font1, 'Contact info:')
        line = self.font1.render('Contact info:', True, Color.white.value)
        self.screen.blit(line, (self.screen_size[0] / 2 - size[0] / 2, 440))
        # Drawing email info
        size = pygame.font.Font.size(self.font1, 'email: robertocarlosmedina.dev@gmail.com')
        line = self.font1.render('email: robertocarlosmedina.dev@gmail.com', True, Color.white.value)
        self.screen.blit(line, (self.screen_size[0] / 2 - size[0] / 2, 450))
        # Drawing GitHub info
        size = pygame.font.Font.size(self.font1, 'Github: https://github.com/RobertoCarlosMedina')
        line = self.font1.render('Github: https://github.com/RobertoCarlosMedina', True, Color.white.value)
        self.screen.blit(line, (self.screen_size[0] / 2 - size[0] / 2, 460))

        self.animation()
        # Controlling if the process of drawing ran 6 times to pass this start page
        if self.count >= 6:
            return "login", None
        return "start", None

    # Method that controls the circle animation display and the time
    def animation(self):
        pos_x, pos_y = int(self.screen_size[0] / 2), int(self.screen_size[1] / 2) + 20
        for i in range(0, 7):
            if i == self.highCircle:
                pygame.draw.circle(self.screen, Color.green1.value, (pos_x - 60, pos_y), 6)
            elif i == self.highCircle + 1:
                pygame.draw.circle(self.screen, Color.green1.value, (pos_x - 60, pos_y), 3)
            elif i == self.highCircle - 1:
                pygame.draw.circle(self.screen, Color.green1.value, (pos_x - 60, pos_y), 3)
            else:
                pygame.draw.circle(self.screen, Color.green2.value, (pos_x - 60, pos_y), 2)
            pos_x += 20

        # Controlling the delay to change the higher circle
        if self.delay >= 100:
            self.highCircle += 1
            self.delay = 0
        self.delay += 1

        # Controlling if the higher circle is at the end to return it to the start
        if self.highCircle > 7:
            self.highCircle = 0
            self.count += 1