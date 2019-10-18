import pygame, time, random

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
car_width= 100
car_height = 150
car_image = pygame.image.load('car.png')
car_image = pygame.transform.scale(car_image, (car_width, car_height))


def borders(border_x, border_y, border_w, border_h, color):
    pygame.draw.rect(gameDisplay, color, [border_x, border_y, border_w, border_h])

def text_objects(text, font):
    text_surf = font.render(text, True, BLACK)
    return text_surf, text_surf.get_rect()

def message_display(text):
    font  = pygame.font.Font('freesansbold.ttf', 100)
    text_surf, text_rect = text_objects(text, font)
    text_rect.center = (WIDTH/2, HEIGHT/2)
    gameDisplay.blit(text_surf, text_rect)
    pygame.display.update()

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

    border_start_x = random.randrange(0, WIDTH)
    border_start_y = -600
    border_speed = 7
    border_width = 100
    border_height = 100

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

        border_start_y += border_speed
        borders(border_start_x, border_start_y, border_width,
                border_height, BLACK)

        if border_start_y > HEIGHT:
            border_start_y = 0-border_width
            border_start_x = random.randrange(0, WIDTH)

        if border_start_y + border_height>y:
            if not x + car_width < border_start_x or not x > border_start_x + border_width:
                crash()

        car(x,y)
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
