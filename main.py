import pygame
from PIL import Image
import importlib.util as imp
import json
from datetime import timedelta
from datetime import datetime

def import_from_current_file(name, path):
    spec = imp.spec_from_file_location(name, path)
    foo = imp.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return foo

pygame.mixer.init()
pygame.init()

tela = pygame.display.set_mode([600, 600])
pygame.display.set_caption("WHATSAPP RUN")
pygame.display.set_icon(pygame.image.load("sprites/icone/sprite.png"))

personagem = import_from_current_file("personagem","sprites/telefone/sprite.py").sprite
personagem = personagem(tela)
sprite_vida = import_from_current_file("sprite_vida", "sprites/vida/sprite.py").sprite(tela, personagem)
cacto = import_from_current_file("cacto", "sprites/cacto/sprite.py").sprite(tela, personagem)

pygame.font.init()
font = pygame.font.SysFont("Arial",20, bold=True)
pause = False
delay = timedelta(seconds = 25)
next = datetime.now()+delay
while True:
    if pause == False:
        tela.blit(pygame.image.load("sprites/background/sprite.png"), [0,0])
        cacto.update()
        personagem.update()
        pontos = json.load(open("data.dat","r", encoding="utf-8"))["pontos"]
        word = font.render(f"Você está com {pontos} pontos", False, (0, 180, 0, 255))
        tela.blit(word, [0,0])
        sprite_vida.update()

    if datetime.now() >= next:
        next = datetime.now()+delay
        cacto.delay /= 2
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            data = {"vida": 3, "pontos":0}
            json.dump(data, open("data.dat", "w", encoding="utf-8"), ensure_ascii=False)
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if pause == False:
                    pause = True
                else:
                    pause = False
    pygame.display.flip()