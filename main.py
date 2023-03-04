import pygame
import os


# Pygame penceresini başlatma
pygame.init()

# Pencere boyutunu belirleme
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Renk tanımları
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Dairelerin saklanacağı liste
circles = []

filename = "screenshot.png"
save_path = os.path.join(os.getcwd(), filename)

def take_screenshot(screen, save_path):
    """
    Takes a screenshot of the current Pygame screen and saves it as a PNG file at the specified path.
    If a file with the same name already exists, adds a number to the end of the filename to make it unique.
    """
    # Check if the file already exists
    if os.path.isfile(save_path):
        # If the file exists, add a number to the end of the filename to make it unique
        i = 1
        while os.path.isfile(save_path[:-4] + '-' + str(i) + save_path[-4:]):
            i += 1
        save_path = save_path[:-4] + '-' + str(i) + save_path[-4:]

    # Take the screenshot and save it to the specified path
    pygame.image.save(screen, save_path)

screenshot_taken = False
# Ana döngü
running = True
while running:

    # Ekrandaki tüm nesneleri temizleme
    screen.fill(WHITE)

    # Fare pozisyonunu al
    mouse_position = pygame.mouse.get_pos()

    # Fare sol düğmesi tıklandı mı kontrol et
    mouse_pressed = pygame.mouse.get_pressed()[0]

    # Fare sol düğmesi tıklandıysa, yeni bir daire ekle
    if mouse_pressed:
        circles.append(mouse_position)

    # Tüm daireleri çiz
    for circle_position in circles:
        pygame.draw.circle(screen, BLACK, circle_position, 5)

    # Ekrandaki tüm nesneleri çizme
    pygame.display.flip()

    
    # "1" tuşuna basıldıysa, çizimi png olarak kaydet
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1] and not screenshot_taken:
        take_screenshot(screen, save_path)
        screenshot_taken = True

    elif not keys[pygame.K_1] and screenshot_taken:
        screenshot_taken = False
  


    elif keys[pygame.K_ESCAPE]:
        running = False
        pygame.quit()
        break

    # Oyunu kapatmak için 'X' düğmesine tıklandı mı kontrol et
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Delete tuşuna basıldıysa, ekrandaki tüm nesneleri temizle
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DELETE:
            circles = []

# Pygame penceresini kapatma
pygame.quit()
