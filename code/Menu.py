#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame.constants import K_DOWN
from pygame.font import Font
from pygame.surface import Surface
from pygame.rect import Rect
from code.Const import WIN_WIDTH, WIN_HEIGTH, C_ORANGE, C_WHITE, MENU_OP, C_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/bg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer.music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)


        while True:

            #DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(75, 'Mountain', C_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(75, 'Shooter', C_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OP)):
                if i == menu_option:
                    self.menu_text(40, MENU_OP[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))

                else:
                    self.menu_text(40, MENU_OP[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()



            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame

                if event.type == pygame.KEYDOWN:
                    if event.key == K_DOWN:
                        if menu_option <len(MENU_OP) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1

                        else:
                            menu_option = len(MENU_OP) - 1

                    if event.key == pygame.K_RETURN: #Enter
                        return MENU_OP[menu_option]


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
