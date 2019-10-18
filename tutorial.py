import pygame, time

pygame.init()

# window properties
WIDTH = 640
HEIGHT = 480
RESOLUTION = WIDTH, HEIGHT

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# window output
gameDisplay = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption('Gonshik nelegalny')
clock = pygame.time.Clock()

# output scaled car image
car_image = pygame.image.load('car.png')
car_image = pygame.transform.scale(car_image, (100, 150))

def text_objects():
    pass

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    text_surf, text_rect = text_objects(text, largeText)
    text_rect.center = (WIDTH/2, HEIGHT/2)
    gameDisplay.blit()

def crash():
    message_display('You crashed')
    time.sleep(2)
    game_loop()

# displays car at certain position
def car(x,y):
    gameDisplay.blit(car_image, (x,y))

def game_loop():

    crashed = False

    # start properties
    x = WIDTH * 0.45
    y = HEIGHT * 0.6
    x_speed = 0

    while not crashed:

        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -5
                elif event.key == pygame.K_RIGHT:
                    x_speed = 5


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_speed = 0

        if x + 100 > WIDTH or x < 0:
            crash()

        # drawing and outputing display
        x += x_speed
        gameDisplay.fill(WHITE)
        car(x,y)
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
