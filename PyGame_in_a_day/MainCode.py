import random
import pygame
pygame.init() # initialise pygame

#set size of screen
WIDTH = 640
HEIGHT = 640
Screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the hero
hero = pygame.sprite.Sprite()

# Add image and rectangle properties to the hero
try: #
    hero.image = pygame.image.load('hero.png')
except:
    hero.image = pygame.image.load('PyGame_in_a_day/hero.png')

#load an sound for the sound effect
try: # the try is to make sure that the image can be loaded when open in vscode in diffrent places
    munch_sound = pygame.mixer.Sound('nom.wav')
except:
    munch_sound = pygame.mixer.Sound('PyGame_in_a_day/nom.wav')

# Set the size for the image
DEFAULT_IMAGE_SIZE = (WIDTH/4, HEIGHT/4)
 
# Scale the image to the right size
hero.image = pygame.transform.scale(hero.image, DEFAULT_IMAGE_SIZE)

hero.rect = hero.image.get_rect()

Hero_group = pygame.sprite.GroupSingle(hero)

TILE_SIZE = hero.rect.width
NUM_TILES_WIDTH = WIDTH / TILE_SIZE
NUM_TILES_HEIGHT = HEIGHT / TILE_SIZE

candies = pygame.sprite.OrderedUpdates() #make a list to store all the candies


def add_candy(candies):
    candy = pygame.sprite.Sprite() #creates a sprite for candy
    #load an image for the candy sprite
    try: # the try is to make sure that the image can be loaded when open in vscode in diffrent places
        candy.image = pygame.image.load('candy.png') 
    except:
        candy.image = pygame.image.load('PyGame_in_a_day/candy.png')
    candy.image= pygame.transform.scale(candy.image, DEFAULT_IMAGE_SIZE)
    candy.rect = candy.image.get_rect()
    candy.rect.left = random.randint(0, int(NUM_TILES_WIDTH) - 1) * TILE_SIZE
    candy.rect.top = random.randint(0, int(NUM_TILES_HEIGHT) - 1) * TILE_SIZE
    candies.add(candy)

for i in range(10):
    add_candy(candies)

pygame.time.set_timer(pygame.USEREVENT, 1000) # add an event to the event queue every certain number of milliseconds

win = False
finish = False
while finish != True:
    for event in pygame.event.get():
        #closes the window when the ESCAPE key is pressesd
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            finish = True
        #closes the window when the X is pressesd
        if event.type == pygame.QUIT:
            finish = True 
        
        # Reads inputs and moves the hero around the screen.
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and hero.rect.top > 0:
                hero.rect.top -= TILE_SIZE
            elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and hero.rect.bottom < HEIGHT:
                hero.rect.top += TILE_SIZE
            elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and hero.rect.right < WIDTH:
                hero.rect.right += TILE_SIZE
            elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and hero.rect.left > 0:
                hero.rect.right -= TILE_SIZE
        
    if event.type == pygame.USEREVENT:
        if win == False:
            add_candy(candies)

    collides = pygame.sprite.groupcollide(Hero_group, candies, False, True)
    if len(collides) > 0:
        munch_sound.play()

    if len(candies) == 0:
        win = True

    # Paint the background black (the three values represent red, green and blue: 0 for all of them makes it black)
    Screen.fill((192, 244, 247))

    if win:
        font = pygame.font.Font(None, 66)
        text_image = font.render("You Win!", True, (0, 0, 0))
        text_rect = text_image.get_rect(centerx=WIDTH/2, centery=100)
        Screen.blit(text_image, text_rect)

    candies.draw(Screen)
    if win == False:
        Hero_group.draw(Screen)
    pygame.display.update()
pygame.quit()

