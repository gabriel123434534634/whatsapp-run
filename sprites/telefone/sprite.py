import pygame
from PIL import Image
from datetime import timedelta
from datetime import datetime
import os
from threading import Thread
pygame.mixer.init()
def Crop_Image(image, rect):
    if type(image) == str:
        image = Image.open(image)
    image = image.crop(rect)
    
    return pygame.image.frombuffer(image.tobytes(), image.size, image.mode)


class sprite:
    def __init__(self, tela, delay=0.1):
        self.tela = tela
        self.fix_delay = delay
        self.delay = delay
        self.índice = 0
        self.tamanho = 30
        self.fix_pos = (270, 500)
        self.pulado = [150, 150]
        self.pos = list(self.fix_pos)
        self.file = Image.open("sprites/telefone/sprite.png")
        self.sprites = {
            "correndo":[
                Crop_Image(self.file, [1, 1, 10, 29]),
                Crop_Image(self.file, [18, 1, 26, 29]),
            ],
            "pulando":[
                Crop_Image(self.file, [1, 32, 9, 59]),
                Crop_Image(self.file, [18, 32, 26, 59]),
                Crop_Image(self.file, [33, 32, 48, 59]),
            ],
        }
        self.direção = "correndo"
        self.image = self.sprites[self.direção][self.índice]
        self.tela.blit(self.image, self.fix_pos)
        self.image = pygame.transform.scale(self.image, [self.image.get_rect()[2]*3, self.image.get_rect()[3]*3])
        self.next = datetime.now()+timedelta(seconds=self.fix_delay)
    def update(self):
        key = pygame.key.get_pressed()
        if (key[pygame.K_SPACE] == 0 and (self.direção == "correndo")):
            if datetime.now() >= self.next:
                self.índice += 1
                if self.índice >= len(self.sprites["correndo"]):
                    self.índice = 0
                self.image = self.sprites[self.direção][self.índice]
                self.next = datetime.now()+timedelta(seconds=self.fix_delay)
            
            self.image = self.sprites[self.direção][self.índice]
            self.image = pygame.transform.scale(self.image, [self.image.get_rect()[2]*3, self.image.get_rect()[3]*3])
            self.tela.blit(self.image, self.fix_pos)
        if (key[pygame.K_SPACE] == 1) and (self.direção == "correndo"):
            channel0 = pygame.mixer.Channel(0)
            channel0.play(pygame.mixer.Sound("sounds/toque.mp3"), 0)
            self.direção = "pulando"
            self.índice = 0
            self.delay = 0.025
            self.next = datetime.now()+timedelta(seconds=self.delay)
            self.image = self.sprites[self.direção][self.índice]
            self.image = pygame.transform.scale(self.image, [self.image.get_rect()[2]*3, self.image.get_rect()[3]*3])
            self.tela.blit(self.image, self.pos)
        if self.direção == "pulando":
            if datetime.now() >= self.next:
                self.índice += 1
                if self.índice >= 2:
                    if self.pulado[0] > 0:
                        self.pos[1] -= self.tamanho
                        self.pulado[0] -= self.tamanho
                    else:
                        self.pos[1] += self.tamanho
                        self.pulado[1] -= self.tamanho
                        if self.pulado[1] <= 0:
                            self.índice = 0
                            self.pos = list(self.fix_pos)
                            self.direção = "correndo"
                            self.pulado = [150, 150]
                self.next = datetime.now()+timedelta(seconds=self.delay)    
            if self.índice >= len(self.sprites[self.direção]):
                self.índice = len(self.sprites[self.direção])-1
            self.image = self.sprites[self.direção][self.índice]
            self.image = pygame.transform.scale(self.image, [self.image.get_rect()[2]*3, self.image.get_rect()[3]*3])
            self.tela.blit(self.image, self.pos)
           