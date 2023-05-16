import pygame
import random
import time

GERI_SAYIM_SURESI = 20
geri_Sayim = GERI_SAYIM_SURESI

def countdown(geri_Sayim):
    while geri_Sayim:
        mins, secs = divmod(geri_Sayim, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        geri_Sayim -= 1


# Ekran boyutları
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PINK= (255, 20, 147)

pygame.init()

# Ekranı oluştur
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Objenin Kaybolup Belirmesi")

# Objeyi oluştur
obje = pygame.Surface((50, 50))
obje.fill(PINK)

# Objeyi rastgele bir konuma yerleştir
obje_x = random.randint(0, SCREEN_WIDTH - obje.get_width())
obje_y = random.randint(0, SCREEN_HEIGHT - obje.get_height())
obje_rect = obje.get_rect().move(obje_x, obje_y)

# Skor değişkeni
skor = 0

# Yüksek çözünürlüklü zamanlayıcı
clock = pygame.time.Clock()

# Objenin kaybolma zamanlayıcısı
kaybolma_zamanlayici = pygame.time.get_ticks() + 1000

# Countdown timer event
COUNTDOWN_EVENT = pygame.USEREVENT + 1

# Set countdown timer
pygame.time.set_timer(COUNTDOWN_EVENT, 1000)

while True:
    # Olayları işle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # sol fare düğmesi tıklandıysa
                fare_x, fare_y = event.pos
                if obje_rect.collidepoint(fare_x, fare_y):  # fare koordinatları obje koordinatları içinde mi?
                    if pygame.mouse.get_pressed()[0]:  # fare düğmesi basılıysa
                        skor += 1

        elif event.type == COUNTDOWN_EVENT:
            geri_Sayim -= 1

        # Objeyi çiz
    screen.fill(BLACK)
    if pygame.time.get_ticks() >= kaybolma_zamanlayici:
        obje_x = random.randint(0, SCREEN_WIDTH - obje.get_width())
        obje_y = random.randint(0, SCREEN_HEIGHT - obje.get_height())
        obje_rect = obje.get_rect().move(obje_x, obje_y)
        kaybolma_zamanlayici = pygame.time.get_ticks() + 1000

    else:
        screen.blit(obje, obje_rect)

    font = pygame.font.SysFont("Arial", 48)
    skor_metni = font.render("skor :" + str(skor), True, (255, 255, 0))
    screen.blit(skor_metni, (3, 3))

    # Ekrana geri sayım süresini yazdır

    font = pygame.font.SysFont("Arial", 48)
    geri_sayim_metni = font.render("time : " + str(geri_Sayim), True, RED)
    screen.blit(geri_sayim_metni, (SCREEN_WIDTH - geri_sayim_metni.get_width() - 10, 10))


    if geri_Sayim <= 0:
        pygame.quit()
        quit()

    if skor > 10:
        time.sleep(1)
        quit()
    elif skor == 10:
        font = pygame.font.SysFont("Arial", 60)
        aferin_metni = font.render("AFERİNNNNN ", True, PINK)
        x = (SCREEN_WIDTH - aferin_metni.get_width()) / 2
        y = (SCREEN_HEIGHT - aferin_metni.get_height()) / 2
        screen.blit(aferin_metni, (x, y))


    pygame.time.set_timer(pygame.USEREVENT, 1000)
    pygame.display.flip()