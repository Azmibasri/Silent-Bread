import pygame
from src.settings import *
from src.dialog import *
from src.tombol_opsi import Opsi
from src.pertanyaa import *
class Game:
    def __init__(self):
        # Inisialisasi modul utama Pygame
        pygame.init()
        
        # Pengaturan jendela game (resolusi dan judul diambil dari settings.py)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        
        # Pengatur waktu (Clock) untuk mengontrol frame rate (FPS)
        self.clock = pygame.time.Clock()
        
        # Status utama aplikasi (True selama game belum ditutup)
        self.running = True

    def new(self):
        # Memulai game baru (Reset level, inisialisasi entitas/sprite)
        # Gunakan sprite group untuk memudahkan update dan render massal
        self.all_sprites = pygame.sprite.Group()

        self.dialog1 = Dialog(self.screen,soal_1["Pesanan"])
        self.btn_opsi1 = Opsi(self.screen,100,400,200,50,soal_1["opsi"][0])
        self.btn_opsi2 = Opsi(self.screen,320,400,200,50,soal_1["opsi"][1])
        self.btn_opsi3 = Opsi(self.screen,540,400,200,50,soal_1["opsi"][2])
        # Contoh inisialisasi objek nanti:
        # self.player = Player()
        # self.all_sprites.add(self.player)
        
        # Mulai Game Loop
        self.run()

    def run(self):
        # Game Loop Utama
        self.playing = True
        while self.playing:
            # 1. Batasi kecepatan game agar stabil sesuai FPS
            self.clock.tick(FPS) 
            
            # 2. Tangkap input dari pemain
            self.events()        
            
            # 3. Perbarui posisi dan logika semua objek
            self.update()        
            
            # 4. Gambar semua perubahan ke layar
            self.draw()          

    def events(self):
        # Menangani semua interaksi sistem dan pemain
        for event in pygame.event.get():
            # Jika user menekan tombol 'X' di pojok jendela
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                
            # Jika user menekan tombol di keyboard
            if event.type == pygame.KEYDOWN:
                # Tombol ESCAPE untuk keluar dari permainan
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self.running = False

            if self.btn_opsi1.is_clicked(event):
                print("Tombol" + self.btn_opsi1.text + "berhasil")
            if self.btn_opsi2.is_clicked(event):
                print("Tombol" + self.btn_opsi2.text + "berhasil")
            if self.btn_opsi3.is_clicked(event):
                print("Tombol" + self.btn_opsi3.text + "berhasil")
    def update(self):
        # Memperbarui semua sprite yang ada di dalam all_sprites group
        # Ini akan otomatis memanggil fungsi update() di dalam setiap class objekmu (misal di player.py)
        self.all_sprites.update()

    def draw(self):
        # Bersihkan layar di setiap frame baru dengan warna background
        self.screen.fill(BG_COLOR)
        
        self.dialog1.draw()
        self.btn_opsi1.draw()
        self.btn_opsi2.draw()
        self.btn_opsi3.draw()
        
        # Gambar seluruh sprite yang ada di grup ke atas kanvas (screen)
        self.all_sprites.draw(self.screen)
        
        # Perbarui tampilan jendela (wajib dipanggil di akhir proses draw)
        pygame.display.flip()

    def show_start_screen(self):
        # TODO: Tambahkan logika layar menu utama (tekan tombol untuk mulai)
        pass

    def show_game_over_screen(self):
        # TODO: Tambahkan logika layar Game Over (skor akhir, tekan tombol untuk main lagi)
        pass