import pygame
import random


# Цвета
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)


pygame.init()

# Main window
winWidth  = 640
winHeight = 480
winSize = [winWidth, winHeight]
screen = pygame.display.set_mode(winSize)

pygame.display.set_caption("Ping Pong")

clock = pygame.time.Clock()
done = False


# Инициализация
    # Игроков
    # Шарика
    # Бонусов

# Основной цикл
while not done:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
                
    # Игровая логика
        # Обработка игроков

        # Пересечение шарика и платформы
        
        # Свободное движение шарика

        # Генерация бонусов
 
        # Пересечение бонуса и платформы


                    
    # Код для рисования
    screen.fill(BLACK) 
    
        # Основной режим игры
        # Конец игры

    pygame.display.flip()      
    clock.tick(60)

pygame.quit()