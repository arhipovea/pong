import pygame
import random


# Цвета
black = (0, 0, 0)
white = (0xFF, 0xFF, 0xFF)
red = (0xFF, 0, 0)


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

# 1 Игрок(Plr1)
widthPlatfPlr1 = 60
heightPlatfPlr1 = 12
speedPlatfPlr1 = 2
coordXPlatfPlr1 = (winWidth-widthPlatfPlr1)/2
platfPlr1L = False
platfPlr1R = False

# 2 Игрок(Plr2)
widthPlatfPlr2 = 60
heightPlatfPlr2 = 12
speedPlatfPlr2 = 2
coordXPlatfPlr2 = (winWidth-widthPlatfPlr2)/2
platfPlr2L = False
platfPlr2R = False
    # Шарика
    # Бонусов

# Основной цикл
while not done:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # Обработка нажатий клавиш "Стрелка влево" и "Стрелка вправо" для управления платформой Игрока 1 и клавиш "A" и "D" для управления платформой Игрока 2
        if event.type == pygame.KEYDOWN:
            # 1
            if event.key == pygame.K_LEFT:
                platfPlr1L = True
            if event.key == pygame.K_RIGHT:
                platfPlr1R = True
            # 2
            if event.key == pygame.K_a:
                platfPlr2L = True
            if event.key == pygame.K_d:
                platfPlr2R = True
                
        if event.type == pygame.KEYUP:
            # 1
            if event.key == pygame.K_LEFT:
                platfPlr1L = False
            if event.key == pygame.K_RIGHT:
                platfPlr1R = False
            # 2
            if event.key == pygame.K_a:
                platfPlr2L = False
            if event.key == pygame.K_d:
                platfPlr2R = False                
    # Игровая логика
    
        # Обработка игроков
        
    # Условие движение платформы Игрока 1
    if platfPlr1L == True:
        coordXPlatfPlr1-=speedPlatfPlr1
        # Обработка левой границы 
        if coordXPlatfPlr1 < 0:
            coordXPlatfPlr1 = 0
            
    if platfPlr1R == True:
        coordXPlatfPlr1+=speedPlatfPlr1
        # Обработка правой границы
        if coordXPlatfPlr1 > winWidth-widthPlatfPlr1:
            coordXPlatfPlr1 = winWidth-widthPlatfPlr1
            
    # Условие движение платформы Игрока 2
    if platfPlr2L == True:
        coordXPlatfPlr2-=speedPlatfPlr2
        # Обработка левой границы 
        if coordXPlatfPlr2 < 0:
            coordXPlatfPlr2 = 0
                        
    if platfPlr2R == True:
        coordXPlatfPlr2+=speedPlatfPlr2
        # Обработка правой границы
        if coordXPlatfPlr2 > winWidth-widthPlatfPlr2:
            coordXPlatfPlr2 = winWidth-widthPlatfPlr2
            
        # Пересечение шарика и платформы
        
        # Свободное движение шарика

        # Генерация бонусов
 
        # Пересечение бонуса и платформы


                    
    # Код для рисования
    screen.fill(white)
    
        # Основной режим игры
    # Прорисовка платформы игрока 1
    pygame.draw.rect(screen, black, [coordXPlatfPlr1, winHeight - (heightPlatfPlr1 + 2), widthPlatfPlr1, heightPlatfPlr1])
    
    # Прорисовка платформы игрока 2
    pygame.draw.rect(screen, black, [coordXPlatfPlr2, 2, widthPlatfPlr2, heightPlatfPlr2])
        # Конец игры

    pygame.display.update()      
    clock.tick(200)

pygame.quit()