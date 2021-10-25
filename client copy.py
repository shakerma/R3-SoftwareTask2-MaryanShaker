import pygame
import sys
import socket
from pygame import QUIT
display = pygame.display.set_mode((500, 500))
pygame.init()
HOST = '127.0.0.1'
PORT = 65433

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                   #direction
                if event.key == pygame.K_w:
                    s.send('w'.encode())
                if event.key == pygame.K_a:
                    s.send('a'.encode())
                if event.key == pygame.K_s:
                    s.send('s'.encode())
                if event.key == pygame.K_d:
                    s.send('d'.encode())
                    #speed
                if event.key == pygame.K_0:
                    s.send('0'.encode())
                if event.key == pygame.K_1:
                    s.send('1'.encode())
                if event.key == pygame.K_2:
                    s.send('2'.encode())
                if event.key == pygame.K_3:
                    s.send('3'.encode())
                if event.key == pygame.K_4:
                    s.send('4'.encode())
                if event.key == pygame.K_5:
                    s.send('5'.encode())
