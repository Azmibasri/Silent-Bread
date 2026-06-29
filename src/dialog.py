import pygame

class Dialog:
    def __init__(self,surface,teks):
        self.teks = teks
        self.surface = surface
        self.rect = pygame.Rect(150,100,500,200)
        self.color = (255,255,255)
        self.text_color = (0,0,0)

        self.font = pygame.font.SysFont('arial',24)

    def draw_text_wrapped(self):
        words = self.teks.split(' ')

        padding = 40
        max_width = self.rect.width - (padding*2)
        x = self.rect.x + padding
        y = self.rect.y + padding

        current_line = ""

        for word in words:
            test_line = current_line + word + " "

            test_width,test_height = self.font.size(test_line)

            if test_width > max_width:
                text_surface = self.font.render(current_line,True,self.text_color)
                self.surface.blit(text_surface,(x,y))

                y += test_height

                current_line = word + " "
            else:
                current_line = test_line

        if current_line:
            text_surface = self.font.render(current_line,True,self.text_color)
            self.surface.blit(text_surface,(x,y))

    def draw(self):
        pygame.draw.rect(self.surface,self.color,self.rect,width=0)
        self.draw_text_wrapped()