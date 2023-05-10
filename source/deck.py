import random, os
import numpy as np

from . import (
    SCREEN_HEIGHT, 
    SCREEN_WIDTH, 
    NUMBER_OF_CARDS, 
    NUMBER_OF_SONGS,
    __assets_folder__
)

from .song import Song 
from .card import Card

song_names = [f'{i}.mp3' for i in range(NUMBER_OF_SONGS)] * 2
 

class Deck:

    def __init__(self, song_folder):                
        song_names = list(filter(lambda x: x.endswith('.mp3'), os.listdir(song_folder)))
        if len(song_names) > NUMBER_OF_SONGS:
            song_names = random.sample(song_names, k=NUMBER_OF_SONGS)        

        self.r = 100
        self.songs = [Song(song_name, song_folder) for song_name in song_names] * 2

        n = int(np.sqrt(NUMBER_OF_CARDS))         
        d = 10
        u = (SCREEN_WIDTH  - (n * self.r + (n - 1) * d)) // 2      
        v = (SCREEN_HEIGHT - (n * self.r + (n - 1) * d)) // 2  

        positions = [
            (int(u + (2 * i + 1) * self.r // 2 + i * d), 
             int(v + (2 * j + 1) * self.r // 2 + j * d)) 
            for i in range(n) for j in range(n)
        ]

        self.cards = [Card(pos, self.r, 'red', song) for pos, song in zip(positions, self.songs)]
        self.clicked_cards = []


    def draw(self, screen):
        for card in self.cards:
            card.draw(screen)

    def shuffle(self):      
        positions = [card.position for card in self.cards] 
        random.shuffle(positions)
        for new_pos, card in zip(positions, self.cards):   
            card.position = new_pos

    def check_match(self):        
        card1, card2 = self.clicked_cards

        if card1 == card2:
            card1.stop_song()
            self.cards.remove(card1)

            card2.stop_song()
            self.cards.remove(card2)   
        else:
            card1.click()
            card2.click()

        self.clicked_cards = []

    def overlap(self, pos):
        for card in self.cards:
            if collide_with_point(card, pos):
                card.click()     
                self.clicked_cards += [card]        

def collide_with_point(card, pos):
    size = card._size
    cx, cy = card.position
    x, y = pos

    if (cx - size//2 <= x <= cx + size//2) and (cy - size//2 <= y <= cy + size//2):
        return True
    else:
        return False
