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
widthPlatfPlr1 = 12
heightPlatfPlr1 = 60
speedPlatfPlr1 = 2
coordYPlatfPlr1 = (winHeight-heightPlatfPlr1)/2
platfPlr1L = False
platfPlr1R = False

# 2 Игрок(Plr2)
widthPlatfPlr2 = 12
heightPlatfPlr2 = 60
speedPlatfPlr2 = 2
coordYPlatfPlr2 = (winHeight-heightPlatfPlr2)/2
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
        coordYPlatfPlr1 -= speedPlatfPlr1
        # Обработка верхней границы 
        if coordYPlatfPlr1 < 0:
            coordYPlatfPlr1 = 0
            
    if platfPlr1R == True:
        coordYPlatfPlr1 += speedPlatfPlr1
        # Обработка нижней границы
        if coordYPlatfPlr1 > winHeight-heightPlatfPlr1:
            coordYPlatfPlr1 = winHeight-heightPlatfPlr1
            
    # Условие движение платформы Игрока 2
    if platfPlr2L == True:
        coordYPlatfPlr2-=speedPlatfPlr2
        # Обработка левой границы 
        if coordYPlatfPlr2 < 0:
            coordYPlatfPlr2 = 0
                        
    if platfPlr2R == True:
        coordYPlatfPlr2+=speedPlatfPlr2
        # Обработка правой границы
        if coordYPlatfPlr2 > winHeight-heightPlatfPlr2:
            coordYPlatfPlr2 = winHeight-heightPlatfPlr2
            
        # Пересечение шарика и платформы
        
        # Свободное движение шарика

        # Генерация бонусов
 
        # Пересечение бонуса и платформы


                    
    # Код для рисования
    screen.fill(white)
    
        # Основной режим игры
    # Прорисовка платформы игрока 1
    pygame.draw.rect(screen, black, [2, coordYPlatfPlr1, widthPlatfPlr1, heightPlatfPlr1])
    
    # Прорисовка платформы игрока 2
    pygame.draw.rect(screen, black, [winWidth-(widthPlatfPlr1+2), coordYPlatfPlr2, widthPlatfPlr2, heightPlatfPlr2])
        # Конец игры

    pygame.display.update()      
    clock.tick(200)

pygame.quit()