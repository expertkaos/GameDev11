import pygame
pygame.init() # initialise pygame

#set size of screen
WIDTH = 640
HEIGHT = 480
Screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the hero
hero = pygame.sprite.Sprite()
# Add image and rectangle properties to the hero
try:
    hero.image = pygame.image.load('hero.png')
except:
    hero.image = pygame.image.load('PyGame_in_a_day/hero.png')
hero.rect = hero.image.get_rect()

Hero_group = pygame.sprite.GroupSingle(hero)

finish = False
while finish != True:
    for event in pygame.event.get():
        #closes the window when the ESCAPE key is pressesd
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            finish = True
        #closes the window when the X is pressesd
        if event.type == pygame.QUIT:
            finish = True      
pygame.quit()

