import pygame
import random

# Идентификация сообщений
def messageToScreen1(msg, color):
    screenText = font.render(msg, True, color)
    textX = screenText.get_rect().width
    textY = screenText.get_rect().height    
    screen.blit(screenText, [winWidth // 2 - textX // 2, winHeight // 2 - textY // 2])
    
def messageToScreen2(msg, color):
    screenText = font.render(msg, True, color)
    textX = screenText.get_rect().width
    textY = screenText.get_rect().height    
    screen.blit(screenText, [winWidth // 2 - textX // 2, textY])

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
font = pygame.font.SysFont(None, 25)
pygame.display.set_caption("Ping Pong")

clock = pygame.time.Clock()

# Основной цикл
def gameLoop():
    # Инициализация
        # Игроков
            # 1 Игрок(Plr1)
    widthPlatfPlr1 = 20
    heightPlatfPlr1 = 100
    speedPlatfPlr1 = 2
    coordYPlatfPlr1 = (winHeight - heightPlatfPlr1)/2
    platfPlr1U = False
    platfPlr1D = False
    scorePlr1 = 0
    listPlr1=[2, coordYPlatfPlr1, widthPlatfPlr1, heightPlatfPlr1]
    
            # 2 Игрок(Plr2)
    widthPlatfPlr2 = 20
    heightPlatfPlr2 = 100
    speedPlatfPlr2 = 2
    coordYPlatfPlr2 = (winHeight - heightPlatfPlr2)/2
    platfPlr2U = False
    platfPlr2D = False
    scorePlr2 = 0
    listPlr2=[winWidth - (widthPlatfPlr1 + 2), coordYPlatfPlr2, widthPlatfPlr2, heightPlatfPlr2]
    
        # 1й шарик
    coordXBall  = winWidth//2
    coordYBall  = winHeight//2
    radiusBall  = 7
    speedXBall  = 1 
    speedYBall  = 1
    
        # 2й шарик
    coordXBall2 = winWidth//3
    coordYBall2 = winHeight//3
    
        # Бонусов
    RandAddBonus = random.randrange(2)
    WidthObjBonus = 10
    HeightObjBonus = 10
    SpeedObjBonus = 2
    FlagBonus = 0
    coordXBonus = winWidth/2
    coordYBonus = random.randrange(480)
    BonusSpeed = 0.5
    BuffTime1 = 0
    BuffTime2 = 0
    FlagBonusTime1 = 0
    FlagBonusTime2 = 0
    
    done = False
    gameOver = False
    display = 0
    
    while not done:
        while gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        done = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
            screen.fill(white)
            if display == 1:
                messageToScreen2("Игрок 1 проиграл :(", black)
            else:
                messageToScreen2("Игрок 2 проиграл :(", black)
            messageToScreen1("GAME OVER, нажмите q, чтобы выйти, или с, чтобы начать игру заново", red)
            pygame.display.update()            
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            # Обработка нажатий клавиш "W" и "S" для управления платформой Игрока 1 и клавиш "Стрелка вверх" и "Стрелка вниз" для управления платформой Игрока 2
            if event.type == pygame.KEYDOWN:
                # 1
                if event.key == pygame.K_w:
                    platfPlr1U = True
                if event.key == pygame.K_s:
                    platfPlr1D = True
                # 2
                if event.key == pygame.K_UP:
                    platfPlr2U = True
                if event.key == pygame.K_DOWN:
                    platfPlr2D = True
                
            if event.type == pygame.KEYUP:
                # 1
                if event.key == pygame.K_w:
                    platfPlr1U = False
                if event.key == pygame.K_s:
                    platfPlr1D = False
                # 2
                if event.key == pygame.K_UP:
                    platfPlr2U = False
                if event.key == pygame.K_DOWN:
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
                
                # Функция рисующая шарик 
        def ball(coordXBall,coordYBall):
            pygame.draw.circle(screen, black, [coordXBall, coordYBall], radiusBall)                
                # Свободное движение шарика
        coordXBall += speedXBall
        coordYBall += speedYBall
       
                # Условие движения бонусов
        if FlagBonus == 1:
            if RandAddBonus == 0:
                coordXBonus = coordXBonus + BonusSpeed
            if RandAddBonus == 1:
                coordXBonus = coordXBonus - BonusSpeed
            if coordXBonus == winWidth:
                BonusSpeed = BonusSpeed * -1
            if coordXBonus == 0:
                BonusSpeed = BonusSpeed * -1    
           
                # Мигание бонуса 
        colorwink = (random.randrange(256), random.randrange(256), random.randrange(256))
                # Генерация бонусов
        BonusFlyTime = 0
        RandBonusLong = random.randrange(5000) 
        if RandBonusLong == 0:
            FlagBonus = 1
            
                # Пересечение бонуса и платформы
           
                # Player 1
        if widthPlatfPlr1 == coordXBonus and coordYPlatfPlr1 + heightPlatfPlr1 > coordYBonus and coordYBonus > coordYPlatfPlr1:
            FlagBonus=0
            coordXBonus = winWidth/2
            coordYBonus = random.randrange(480) 
            BonusSpeed = BonusSpeed * -1
            heightPlatfPlr1 = 140
            FlagBonusTime1 = 1
    
                # Player 2
        if winWidth - widthPlatfPlr2 == coordXBonus and coordYPlatfPlr2 + heightPlatfPlr2 > coordYBonus and coordYBonus > coordYPlatfPlr2: 
            FlagBonus=0
            coordXBonus = winWidth/2
            coordYBonus = random.randrange(480) 
            BonusSpeed = BonusSpeed * -1
            heightPlatfPlr2 = 140
            FlagBonusTime2 = 1
            
                # Время эффекта бонуса 
        if FlagBonusTime1 == 1:
            BuffTime1 = BuffTime1 + 1
        if BuffTime1 == 1500:
            FlagBonus = 1
            BuffTime1 = 0
            heightPlatfPlr1 = 100
        if FlagBonusTime2 == 1:
            BuffTime2 = BuffTime2 + 1   
        if BuffTime2 == 1500:
            FlagBonus = 1
            BuffTime2 = 0
            heightPlatfPlr2 = 100
            
            # Пересечение шарика и платформы
                # А)От первого игрока
        if widthPlatfPlr1 > coordXBall - radiusBall and coordYPlatfPlr1 + (heightPlatfPlr1/5) > coordYBall and coordYBall > coordYPlatfPlr1:
            speedXBall *= -1
            speedYBall *=-2
            scorePlr1 += 1 
            
        if widthPlatfPlr1 > coordXBall - radiusBall and coordYPlatfPlr1 + 2*(heightPlatfPlr1/5) > coordYBall and coordYBall > coordYPlatfPlr1 + (heightPlatfPlr1/5):
            speedXBall *= -1
            scorePlr1 += 1                
        if widthPlatfPlr1 > coordXBall - radiusBall and coordYPlatfPlr1 + 3*(heightPlatfPlr1/5) > coordYBall and coordYBall > coordYPlatfPlr1 + 2*(heightPlatfPlr1/5):
            speedXBall *= -2
            scorePlr1 += 1 
            
        if widthPlatfPlr1 > coordXBall - radiusBall and coordYPlatfPlr1 + 4*(heightPlatfPlr1/5) > coordYBall and coordYBall > coordYPlatfPlr1 + 3*(heightPlatfPlr1/5):
            speedXBall *= -1
            scorePlr1 += 1
                        
        if widthPlatfPlr1 > coordXBall - radiusBall and coordYPlatfPlr1 + heightPlatfPlr1 > coordYBall and coordYBall > coordYPlatfPlr1 + 4*(heightPlatfPlr1/5):
            speedXBall *= -1
            speedYBall *=2
            scorePlr1 += 1 
            
            
           #Отскакивание от боковых частей для 1 платформы 
        if widthPlatfPlr1 > coordXBall - radiusBall and coordYPlatfPlr1 == coordYBall :
            speedXBall =1
            speedYBall =-3
            scorePlr1 += 1 
        if widthPlatfPlr1 > coordXBall - radiusBall and coordYPlatfPlr1+heightPlatfPlr1 == coordYBall :
            speedXBall =1
            speedYBall =3
            scorePlr1 += 1            
                
                 # Б)От второго игрока  
        if winWidth - widthPlatfPlr2 - radiusBall < coordXBall and coordYPlatfPlr2 + (heightPlatfPlr2/5) > coordYBall and coordYBall > coordYPlatfPlr1:
            speedXBall *= -1
            speedYBall *=-2
            scorePlr2 += 1 
        if winWidth - widthPlatfPlr2 - radiusBall < coordXBall and coordYPlatfPlr2 + 2*(heightPlatfPlr2/5) > coordYBall and coordYBall > coordYPlatfPlr2 + (heightPlatfPlr2/5):
            speedXBall *= -1
            scorePlr2 += 1
        if winWidth - widthPlatfPlr2 - radiusBall < coordXBall and coordYPlatfPlr2+ 3*(heightPlatfPlr2/5) > coordYBall and coordYBall > coordYPlatfPlr2 + 2*(heightPlatfPlr2/5):
            speedXBall *= -2
            scorePlr2 += 1    
        if winWidth - widthPlatfPlr2 - radiusBall < coordXBall and coordYPlatfPlr2 + 4*(heightPlatfPlr2/5) > coordYBall and coordYBall > coordYPlatfPlr2 + 3*(heightPlatfPlr2/5):
            speedXBall *= -1
            scorePlr2 += 1                
        if winWidth - widthPlatfPlr2 - radiusBall < coordXBall and coordYPlatfPlr2 + heightPlatfPlr2 > coordYBall and coordYBall > coordYPlatfPlr2 + 4*(heightPlatfPlr2/5):
            speedXBall *= -1
            speedYBall =2
            scorePlr2 += 1 
            
            #Отскакивание от боковых частей для 2 платформы 
        if winWidth - widthPlatfPlr2 - radiusBall < coordXBall and coordYPlatfPlr1 == coordYBall :
            speedXBall *=-1
            speedYBall *=-3
            scorePlr2 += 1 
        if winWidth - widthPlatfPlr2 - radiusBall < coordXBall and coordYPlatfPlr1+heightPlatfPlr1 == coordYBall :
            speedXBall *=1
            speedYBall *=3
            scorePlr2 += 1                  
                        
            
                 # В)От пола  
        if coordYBall + radiusBall > winHeight:
            speedYBall *= -1
                
                 # Г)От потолка
        if coordYBall-radiusBall < 0: 
            speedYBall *= -1
            
        # Условие проигрыша
        if coordXBall + radiusBall > winWidth:
            gameOver = True
            display = 2
        if coordXBall - radiusBall < 0:
            gameOver = True
            display = 1
            
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
        ball(coordXBall, coordYBall)
                
                # Прорисовка бонусов 
        if FlagBonus == 1:
            pygame.draw.rect(screen, colorwink, [coordXBonus, coordYBonus, WidthObjBonus, HeightObjBonus]) 
            
        pygame.display.update()      
        clock.tick(200)
        
gameLoop()

pygame.quit()
quit()
