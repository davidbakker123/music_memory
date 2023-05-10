import pygame
import os
import sys

from source import SCREEN_HEIGHT, SCREEN_WIDTH, __assets_folder__, __songs_folder__
from source.deck import Deck

if __name__ == '__main__':

    if len(sys.argv) > 1:
        if sys.argv[1] == 'beatles':
            song_folder = os.path.join(__songs_folder__, 'beatles')
        elif sys.argv[1] == 'k3':
            song_folder = os.path.join(__songs_folder__, 'k3')
    else: 
        song_folder = os.path.join(__songs_folder__, 'default')


    ## Initialize and shuffle the deck of cards
    deck = Deck(song_folder)  
    deck.shuffle() 

    print([card.song.name for card in deck.cards])

    ## Initialize pygame stuff
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 30)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_img = pygame.image.load(os.path.join(__assets_folder__, 'images', 'background.png'))

    clock = pygame.time.Clock()

    running = True

    ## Main game loop
    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                deck.overlap(mouse_pos)

        screen.blit(bg_img, (0, 0))
        deck.draw(screen)

        pygame.display.flip()

        if len(deck.clicked_cards) == 2:
            deck.check_match()

        clock.tick(30)

    pygame.quit()