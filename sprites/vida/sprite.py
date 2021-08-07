import pygame
from PIL import Image
from datetime import timedelta
from datetime import datetime
import os, json
pygame.mixer.init()
def Crop_Image(image, rect):
    if type(image) == str:
        image = Image.open(image)
    image = image.crop(rect)
    
    return pygame.image.frombuffer(image.tobytes(), image.size, image.mode)

class sprite:
    def __init__(self, tela, personagem,delay=0.01):
        pontos = json.load(open("data.dat","r", encoding="utf-8"))["pontos"]
        self.vida = json.load(open("data.dat","r", encoding="utf-8"))["vida"]
        if self.vida > 3:
            data = {"vida": 3, "pontos":pontos}
            json.dump(data, open("data.dat", "w", encoding="utf-8"), ensure_ascii=False)
            self.vida = 3
        self.tela = tela
        self.índice = 0
        self.image = pygame.image.load("sprites/vida/sprite.png")
        self.sprite = pygame.transform.scale(self.image, [self.image.get_rect()[2]*3, self.image.get_rect()[3]*3])
        self.fix_pos = (0, 30)
        self.pos = list(self.fix_pos)
        for i in range(0, self.vida):
            self.tela.blit(self.image, self.pos)
            self.pos[0] += self.image.get_rect()[2]+5
        self.pos = list(self.fix_pos)
        self.delay = delay
        self.fix_pos_sprite = (2000, 500)
        self.pos_sprite = list(self.fix_pos_sprite)
        self.next = datetime.now()+timedelta(seconds=self.delay)
        self.tela.blit(self.sprite, self.pos)
        self.tamanho = 10
        self.personagem = personagem
    def update(self):
        rect_sprite = self.sprite.get_rect()
        rect_sprite[0] = self.pos_sprite[0]
        rect_sprite[1] = self.pos_sprite[1]
        
        rect_personagem = self.personagem.image.get_rect()
        rect_personagem[0] = self.personagem.pos[0]
        rect_personagem[1] = self.personagem.pos[1]
        
        
        if rect_sprite.colliderect(rect_personagem):
            self.pos_sprite = list(self.fix_pos_sprite)
            self.vida = json.load(open("data.dat","r", encoding="utf-8"))["vida"]
            self.vida += 1
            pontos = json.load(open("data.dat","r", encoding="utf-8"))["pontos"]+1
            data = {"vida":self.vida, "pontos":pontos}
            json.dump(data, open("data.dat", "w", encoding="utf-8"), ensure_ascii=False)
            pygame.mixer.music.load("sounds/assobio.mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
            
        if datetime.now() >= self.next:
            self.pos_sprite[0] -= self.tamanho
            if self.pos[0] < 0:
                self.pos_sprite = list(self.fix_pos_sprite)
            self.next = datetime.now()+timedelta(seconds=self.delay)
    
        self.tela.blit(self.sprite, self.pos_sprite)
        if self.pos_sprite[0] < 0:
            self.pos_sprite = list(self.fix_pos_sprite)
        self.vida = json.load(open("data.dat","r", encoding="utf-8"))["vida"]
        pontos = json.load(open("data.dat","r", encoding="utf-8"))["pontos"]
        if self.vida <= 0:
            data = {"vida": 3, "pontos":0}
            json.dump(data, open("data.dat", "w", encoding="utf-8"), ensure_ascii=False)
        if self.vida > 3:
            data = {"vida": 3, "pontos":pontos}
            json.dump(data, open("data.dat", "w", encoding="utf-8"), ensure_ascii=False)
            self.vida = 3
        self.pos = list(self.fix_pos)
        for i in range(0, self.vida):
            self.tela.blit(self.image, self.pos)
            self.pos[0] += self.image.get_rect()[2]+5
        self.pos = list(self.fix_pos)
        