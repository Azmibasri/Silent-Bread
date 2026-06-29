import pygame

class Opsi:
    def __init__(self,surface,x,y,width,height,text):
        self.surface = surface
        self.rect = pygame.Rect(x,y,width,height)
        self.text = text

        self.color_normal = (70,70,70)
        self.color_hover = (100,100,100)
        self.text_color = (255,255,255)

        self.font = pygame.font.SysFont('arial',24)

        self.is_hovered = False

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.is_hovered = True
            current_color = self.color_hover
        else:
            self.is_hovered = False
            current_color = self.color_normal

        pygame.draw.rect(self.surface,current_color,self.rect)

        text_surface = self.font.render(self.text,True,self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.surface.blit(text_surface,text_rect)

    def is_clicked(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovered:
                return True
        return False