import pygame
import os
import re

mylist = []


def name(n):
    font = pygame.font.SysFont("ALGERIAN", 40)
    song = font.render(mylist[n], True, (128, 0, 0))
    screen.blit(song, [240, 650])
    pygame.display.update()


with os.scandir() as entries:
    for entry in entries:
        if entry.is_file():
            if re.findall(".mp3", entry.name):
                mylist.append(entry.name)

print(mylist)
pygame.init()
pygame.mixer.init()

size = weight, height = (700, 700)

ORANGE = (230, 230, 250)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("music player")

screen.fill(ORANGE)

font = pygame.font.SysFont("ALGERIAN", 75)

text = font.render("music player", True, (139, 0, 0))

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load(mylist[0])
pygame.mixer.music.play()

done = False
pause = False
cnt = 0
pos = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            cnt += 1
            if cnt == 2:
                cnt = 0
            else:
                pos += cnt
                pygame.mixer.music.load(mylist[pos])
                pygame.mixer.music.play()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            cnt += 1
            if cnt == 2:
                cnt = 0
            else:
                pos -= cnt
                pygame.mixer.music.load(mylist[pos])
                pygame.mixer.music.play()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            pause = not pause
            if pause:
                pygame.mixer.music.pause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            pause = not pause
            if not pause:
                pygame.mixer.music.unpause()
        if event.type == SONG_END:
            cnt += 1
            if cnt == 2:
                cnt = 0
            else:
                pos += cnt
                pygame.mixer.music.load(mylist[0])
                pygame.mixer.music.play()
                cnt = 0
    name(pos)
    screen.fill(ORANGE)
    screen.blit(text, (85, 100))
    pygame.display.update()

pygame.quit()