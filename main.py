import pygame
import sys
# UBAH BAGIAN INI: Ambil Game dari dalam folder src
from src.game import Game 

if __name__ == "__main__":
    g = Game()
    g.show_start_screen()
    
    while g.running:
        g.new()
        if g.running:
            g.show_game_over_screen()
            
    pygame.quit()
    sys.exit()