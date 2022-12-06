from abc import ABC, abstractmethod
import pygame as pg


# classe abstrata button
# :parametros:
# :metodos:
class Button(ABC):
    def __init__(self, text_input, font_position_x, font_position_y, font_color, font, screen, left, top, width, height, fill, button_color, shadow_color):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.font = font
        self.font_color = font_color
        self.text_input = text_input
        self.font_position_x = font_position_x
        self.font_position_y = font_position_y
        self.fill = fill
        self.text = font.render(self.text_input, True, self.font_color)
        self.pressed = False
        self.screen = screen
        self.button_color = button_color
        self.shadow_color = shadow_color

    def update(self):
        pg.draw.rect(self.screen, self.shadow_color, (self.left + 5, self.top + 5, self.width, self.height), self.fill)
        pg.draw.rect(self.screen, self.button_color, (self.left, self.top, self.width, self.height), self.fill)
        self.screen.blit(self.text, (self.font_position_x, self.font_position_y))

    def hover(self, position):
        if position[0] in range(self.left, (self.left+self.width)) and position[1] in range(self.top, (self.top+self.height)):
            pg.draw.rect(self.screen, self.button_color, (self.left, self.top, self.width, self.height))
            self.text = self.font.render(self.text_input, True, self.shadow_color)
            self.screen.blit(self.text, (self.font_position_x, self.font_position_y))

        else:
            pg.draw.rect(self.screen, self.button_color, (self.left, self.top, self.width, self.height), self.fill)
            self.text = self.font.render(self.text_input, True, self.font_color)

    def check_click(self, position):
        if position[0] in range(self.left, (self.left + self.width)) and position[1] in range(self.top, (self.top + self.height)):
            return True
        return False

    @abstractmethod
    def action(self, position):
        pass


# CLASSE BUTTON RESTART
class ButtonRestart(Button):
    def __init__(self, text_input, font_position_x, font_position_y, font_color, font, screen, left, top, width, height, fill, button_color, shadow_color):
        super().__init__(text_input, font_position_x, font_position_y, font_color, font, screen, left, top, width, height, fill, button_color, shadow_color)

    def action(self, position, tabuleiro_preenchido=None, escondendo_numeros=None, tabuleiro_data=None, jogo_data=None, function=None):
        if position[0] in range(self.left, (self.left + self.width)) and position[1] in range(self.top, (self.top + self.height)):
            if pg.mouse.get_pressed()[0]:
                pg.draw.rect(self.screen, self.button_color, (self.left, self.top, self.width, self.height), self.fill)
                self.pressed = True
            else:
                if self.pressed:
                    pg.draw.rect(self.screen, self.button_color, (self.left, self.top, self.width, self.height), self.fill)
                    tabuleiro_preenchido = True
                    escondendo_numeros = True
                    tabuleiro_data = function()
                    jogo_data = function()
                    self.pressed = False

        return tabuleiro_preenchido, escondendo_numeros, tabuleiro_data, jogo_data


# CLASSE BUTTON ADD FILE
class ButtonAddFile(Button):
    def __init__(self, text_input, font_position_x, font_position_y, font_color, font, screen, left, top, width, height, fill, button_color, shadow_color):
        super().__init__(text_input, font_position_x, font_position_y, font_color, font, screen, left, top, width, height, fill, button_color, shadow_color)

    def action(self, position, function=None):
        tabuleiro_file = None
        if position[0] in range(self.left, (self.left + self.width)) and position[1] in range(self.top, (self.top + self.height)):
            if pg.mouse.get_pressed()[0]:
                pg.draw.rect(self.screen, self.button_color, (self.left, self.top, self.width, self.height), self.fill)
                self.pressed = True
            else:
                if self.pressed:
                    pg.draw.rect(self.screen, self.button_color, (self.left, self.top, self.width, self.height), self.fill)
                    tabuleiro_file = function()
                    self.pressed = False

        return tabuleiro_file


# CLASSE BUTTON SOLVE
class ButtonSolve(Button):
    def __init__(self, text_input, font_position_x, font_position_y, font_color, font, screen, left, top, width, height, fill, button_color, shadow_color):
        super().__init__(text_input, font_position_x, font_position_y, font_color, font, screen, left, top, width, height, fill, button_color, shadow_color)

    def action(self, position):
        if position[0] in range(self.left, (self.left + self.width)) and position[1] in range(self.top, (self.top + self.height)):
            if pg.mouse.get_pressed()[0]:
                pg.draw.rect(self.screen, self.button_color, (self.left, self.top, self.width, self.height), self.fill)
                self.pressed = True
            else:
                if self.pressed:
                    pg.draw.rect(self.screen, self.button_color, (self.left, self.top, self.width, self.height), self.fill)
                    self.pressed = False


class ButtonMenu(Button):
    def __init__(self, text_input, font_position_x, font_position_y, font_color, font, screen, left, top, width, height, fill, button_color, shadow_color):
        super().__init__(text_input, font_position_x, font_position_y, font_color, font, screen, left, top, width, height, fill, button_color, shadow_color)

    def action(self, position):
        pass