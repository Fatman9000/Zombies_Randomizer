import time
import pygame
import random
import math
import PygameTWF
import PygameCTBF
import extraInfo

pygame.init()
check = False
window = pygame.display.set_mode([800,800])
Type = pygame.font.SysFont("impact", 80)
Type2 = pygame.font.SysFont("Playfair Display",50)
Type3 = pygame.font.SysFont("Tahoma",15)
previous_click = False
cyan_timer = 0
second_screen = False

clock = pygame.time.Clock()
while True:
    window.fill((119, 119, 119))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    window.fill((140,140,140))
    Click = pygame.mouse.get_pressed()

    # Generate Button
    if second_screen is False:
        pygame.draw.rect(window, (230,20,20),(145,145,500,500))
        pygame.draw.rect(window, (0,0,0),(145,145,500,500),5)
        generateC = Type.render("Generate", True, (0,0,0))
        window.blit(generateC, (245,300))
        gChallenge = Type.render("Challenge", True, (0,0,0))
        window.blit(gChallenge, (231,400))

    # Determining if the user is on the second screen or not
    if pygame.mouse.get_pos()[0] >= 200 and pygame.mouse.get_pos()[0] <= 600 and pygame.mouse.get_pos()[1] >= 200 and pygame.mouse.get_pos()[1] <= 600 and second_screen == False and previous_click == False and Click[0]:
        second_screen = True
        mapNumber = random.randint(0,8)
        challengeNumber = random.randint(0,13)

    #Second Screen
    if second_screen:
       
        #Redo Button
        if pygame.mouse.get_pos()[0] >= 690 and pygame.mouse.get_pos()[0] <= 790 and pygame.mouse.get_pos()[1] >= 10 and pygame.mouse.get_pos()[1] <= 60 and previous_click == False and Click[0]:
            mapNumber = random.randint(0,8)
            challengeNumber = random.randint(0,13)
            cyan_timer = 3
        if cyan_timer > 0:
            pygame.draw.rect(window, (50,50,50), (690,10,100,50))
            cyan_timer = cyan_timer - 1
        else:
            pygame.draw.rect(window, (80,80,80),(690,10,100,50))
        pygame.draw.rect(window, (30,30,30), (690,10,100,50),5)
        redo = Type2.render("redo",True, (0,0,0))
        window.blit(redo, (703,18))
        #Challenge Rule Boxes
        # rectdraw2 = 8
        for x in range(0, 8, -1):
            pygame.draw.rect(window, (30,30,30), (10,50 + x * 50,35,35),5)
        for index, amount in enumerate(extraInfo.bDescriptions):
            bDRender = Type2.render(amount,True,(0,0,0))
            window.blit(bDRender, (50,100 + index * 50))
        pygame.draw.line(window, (0,0,0),(0,90),(360,90),5)
        pygame.draw.line(window, (0,0,0),(0,494),(360,494),5)

        #Excluding challenges on certain maps  
        while check is False:
            if challengeNumber == 4 and (mapNumber != 4 or mapNumber != 8):
                mapNumber = random.randint(0,8)
                challengeNumber = random.randint(0,13)
                continue
            if mapNumber == 3 and challengeNumber in [1,2,5,6,11]:
                mapNumber = random.randint(0,8)
                challengeNumber = random.randint(0,13)
                continue
            if mapNumber == 2 and challengeNumber in [5,6,11]:
                mapNumber = random.randint(0,8)
                challengeNumber = random.randint(0,13)
                continue
            if mapNumber == 8 and challengeNumber == 12:
                mapNumber = random.randint(0,8)
                challengeNumber = random.randint(0,13)
                continue
            check = True

        # Challenge Descriptions
        PygameTWF.renderTextWrap((extraInfo.cDescriptions[challengeNumber]), Type2, (0,0,0), 795, window, 0,503,50)

        #Red and Green Boxes 
        
        for index, amount in enumerate(extraInfo.redGreen[challengeNumber]):
            pygame.draw.rect(window, (amount), (15,105 + index * 50,25,25))

        # Displaying the Map and Challenge
        mapName = Type2.render(str(extraInfo.map_name[mapNumber]), True, (0,0,0))
        challengeName = Type2.render(str(extraInfo.challenge[challengeNumber]),True, (0,0,0))
        window.blit(mapName, (10,10))
        window.blit(challengeName, (10,50))

        #Fps Counter
        fPS = Type3.render(str(math.trunc(clock.get_fps())) + " fps", True, (0,0,0))
        window.blit(fPS, (755,780))
    
        # Extra info on hover
        if pygame.mouse.get_pos()[0] < 435 and pygame.mouse.get_pos()[1] > 105 and pygame.mouse.get_pos()[1] < 505:
            for x, y in extraInfo.rangesList:
                if x <= pygame.mouse.get_pos()[1] < y:
                    displayExtraInfo = extraInfo.rangesList.index((x,y))
            PygameCTBF.cursorTextBox((extraInfo.extraInfoDesc[displayExtraInfo]),Type3,(0,0,0),200,window,15,(190,190,190))

    previous_click = Click[0]
    pygame.display.flip()
    clock.tick(30)
pygame.quit()