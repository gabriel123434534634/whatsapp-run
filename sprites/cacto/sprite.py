import pygame
from PIL import Image
from datetime import timedelta
from datetime import datetime
import os
import json
def Crop_Image(image, rect):
    if type(image) == str:
        image = Image.open(image)
    image = image.crop(rect)
    return pygame.image.frombuffer(image.tobytes(), image.size, image.mode)

class sprite:
    def __init__(self, tela, personagem,delay=0.001):
        self.personagem = personagem
        self.tela = tela
        self.delay = delay
        self.image = pygame.image.load("sprites/cacto/sprite.png")
        self.image = pygame.transform.scale(self.image, [int(self.image.get_rect()[2]*0.6), int(self.image.get_rect()[3]*2)])
        self.next = datetime.now()+timedelta(seconds=self.delay)
        self.pos = [800, 500]
        self.fix_pos = tuple(self.pos)
        self.tela.blit(self.image, self.pos)
        self.tamanho = 10
    def update(self):
        rect_personagem = self.personagem.image.get_rect()
        rect_personagem[0] = self.personagem.pos[0]
        rect_personagem[1] = self.personagem.pos[1]
        
        rect = self.image.get_rect()
        rect[0] = self.pos[0]
        rect[1] = self.pos[1]
        
        if rect.colliderect(rect_personagem):
            data = json.load(open("data.dat","r", encoding="utf-8"))
            data["vida"] -= 1
            json.dump(data, open("data.dat", "w", encoding="utf-8"), ensure_ascii=False)
            self.pos = list(self.fix_pos)
        
        if datetime.now() >= self.next:
            self.next = datetime.now()+timedelta(seconds=self.delay)
            self.pos[0] -= self.tamanho
            self.tela.blit(self.image, self.pos)
            if self.pos[0] < 0:
                self.pos[0] = 800
        else:
            self.tela.blit(self.image, self.pos)