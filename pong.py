import pygame
import random


# Цвета
black = (0, 0, 0)
white = (0xFF, 0xFF, 0xFF)
red = (0xFF, 0, 0)
siniy = (0, 0, 0xFF)


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
coordYPlatfPlr1 = (winHeight - heightPlatfPlr1)/2
platfPlr1U = False
platfPlr1D = False
scorePlr1 = 0
listPlr1=[2, coordYPlatfPlr1, widthPlatfPlr1, heightPlatfPlr1]

        # 2 Игрок(Plr2)
widthPlatfPlr2 = 12
heightPlatfPlr2 = 60
speedPlatfPlr2 = 2
coordYPlatfPlr2 = (winHeight - heightPlatfPlr2)/2
platfPlr2U = False
platfPlr2D = False
scorePlr2 = 0
listPlr2=[winWidth - (widthPlatfPlr1 + 2), coordYPlatfPlr2, widthPlatfPlr2, heightPlatfPlr2]

    # Шарика
coordXBall = winWidth//2
coordYBall = winHeight//2
radiusBall = 7
speedXBall = 1 
speedYBall = 1

    # Конца Игры
gameOverPlr1 = False
gameOverPlr2 = False

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
                platfPlr1U = True
            if event.key == pygame.K_RIGHT:
                platfPlr1D = True
            # 2
            if event.key == pygame.K_a:
                platfPlr2U = True
            if event.key == pygame.K_d:
                platfPlr2D = True
                
        if event.type == pygame.KEYUP:
            # 1
            if event.key == pygame.K_LEFT:
                platfPlr1U = False
            if event.key == pygame.K_RIGHT:
                platfPlr1D = False
            # 2
            if event.key == pygame.K_a:
                platfPlr2U = False
            if event.key == pygame.K_d:
                platfPlr2D = False 
            
    # Игровая логика
        # Обработка игроков
            # Условие движение платформы Игрока 1
    if platfPlr1U == True:
        coordYPlatfPlr1 -= speedPlatfPlr1
            # Обработка верхней границы 
        if coordYPlatfPlr1 < 0:
            coordYPlatfPlr1 = 0
            
    if platfPlr1D == True:
        coordYPlatfPlr1 += speedPlatfPlr1
            # Обработка нижней границы
        if coordYPlatfPlr1 > winHeight - heightPlatfPlr1:
            coordYPlatfPlr1 = winHeight - heightPlatfPlr1
            
            # Условие движение платформы Игрока 2
    if platfPlr2U == True:
        coordYPlatfPlr2 -= speedPlatfPlr2
            # Обработка верхней границы 
        if coordYPlatfPlr2 < 0:
            coordYPlatfPlr2 = 0
                        
    if platfPlr2D == True:
        coordYPlatfPlr2 += speedPlatfPlr2
            # Обработка нижней границы
        if coordYPlatfPlr2 > winHeight - heightPlatfPlr2:
            coordYPlatfPlr2 = winHeight - heightPlatfPlr2
            
        # Свободное движение шарика
    coordXBall += speedXBall
    coordYBall += speedYBall
   
        # Генерация бонусов
        
        # Пересечение бонуса и платформы
 
        # Пересечение шарика и платформы
            # А)От первого игрока
    if widthPlatfPlr1 == coordXBall - radiusBall and coordYPlatfPlr1 + heightPlatfPlr1 > coordYBall and coordYBall > coordYPlatfPlr1:
        speedXBall *= -1
        scorePlr1 += 1
            
             # Б)От второго игрока  
    if winWidth - widthPlatfPlr2 - radiusBall == coordXBall and coordYPlatfPlr2 + heightPlatfPlr2 > coordYBall and coordYBall > coordYPlatfPlr2:
        speedXBall *= -1
        scorePlr2 += 1
        
             # В)От пола  
    if coordYBall + radiusBall == winHeight:
        speedYBall *= -1
            
             # Г)От потолка
    if coordYBall == radiusBall: 
        speedYBall *= -1    

        # Условие GameOver'a Игрока 1
    if coordXBall == radiusBall:
        gameOverPlr1 = True
        
        # Условие GameOver'a Игрока 2
    elif coordXBall + radiusBall == winWidth:
        gameOverPlr2 = True 
        
    # Код для рисования
    screen.fill(white)
    
        # Основной режим игры
            # Выведение кол-ва очков, набранных Игроком 1
    plr1Font = pygame.font.SysFont("Calibri", 17)
    textScrPlr1 = plr1Font.render("Счёт 1 Игрока: " + str(scorePlr1), True, red)
    screen.blit(textScrPlr1, [5, 1])
    
            # Выведение кол-ва очков, набранных Игроком 2
    plr2Font = pygame.font.SysFont("Calibri", 17)
    textScrPlr2 = plr2Font.render("Счёт 2 Игрока: " + str(scorePlr2), True, siniy)
    screen.blit(textScrPlr2, [510, 1])    
    
            # Прорисовкаплатформы Игрока 1
    pygame.draw.rect(screen, red, [2, coordYPlatfPlr1, widthPlatfPlr1, heightPlatfPlr1])
    
            # Прорисовка платформы Игрока 2
    pygame.draw.rect(screen, siniy, [winWidth - (widthPlatfPlr1 + 2), coordYPlatfPlr2, widthPlatfPlr2, heightPlatfPlr2])
    
            # Прорисовка шарика
    pygame.draw.circle(screen, black, [coordXBall, coordYBall], radiusBall)
    
    
        # Конец игры
            # Случай проигрыша Игрока 1
    if gameOverPlr1 == True:
        screen.fill(white)
        gameOverFont = pygame.font.SysFont("Calibri", 20)
        textGmOvPlr1 = gameOverFont.render("Игрок 1 проиграл :( Итоговый счёт Игрока 1: " + str(scorePlr1) + " Итоговый счёт Игрока 2: " + str(scorePlr2), True, black)
        screen.blit(textGmOvPlr1, [5, 210])
        
            # Случай проигрыша Игрока 2    
    if gameOverPlr2 == True:
        screen.fill(white)
        gameOverFont = pygame.font.SysFont("Calibri", 20)
        textGmOvPlr2 = gameOverFont.render("Игрок 2 проиграл :( Итоговый счёт Игрока 1: " + str(scorePlr1) + " Итоговый счёт Игрока 2: " + str(scorePlr2), True, black)
        screen.blit(textGmOvPlr2, [5, 210])
        
    pygame.display.update()      
    clock.tick(200)

pygame.quit()
