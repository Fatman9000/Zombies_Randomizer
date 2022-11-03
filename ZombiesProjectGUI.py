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
previousClick = False
cyanTimer = 0
run = True
secondScreen = False
Challenge = ["2 Box","No Jugg","Only Jugg","Melee Only","EE Speedrun","Pap all Weapons","321 Challenge","No Open Doors","Box Roulette","Explosives Only","Wall Weapons Only","No Pack-a-Punch","Olympia Only","Spawn Room"]
Map = ["Town","Farm","Tranzit","Bus Depot","Mob","Buried","Die Rise","Nuketown","Origins"]
bDescriptions = ["Quick Revive/Afterlife","Starting Pistol","Melee/Knifing","Melee/Knife Upgrades","Hells Retriever","Equipment","Non-lethal Buildables","Lethal Buildables"]
rangesList = [(95,145),(145,195),(195,245),(245,295),(295,345),(345,395),(395,445),(445,495)]

clock = pygame.time.Clock()
while run:
    window.fill((119, 119, 119))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.fill((140,140,140))
    Click = pygame.mouse.get_pressed()

    # Generate Button
    if secondScreen == False:
        pygame.draw.rect(window, (230,20,20),(145,145,500,500))
        pygame.draw.rect(window, (0,0,0),(145,145,500,500),5)
        generateC = Type.render("Generate", True, (0,0,0))
        window.blit(generateC, (245,300))
        gChallenge = Type.render("Challenge", True, (0,0,0))
        window.blit(gChallenge, (231,400))

    # Determining if the user is on the second screen or not
    if pygame.mouse.get_pos()[0] >= 200 and pygame.mouse.get_pos()[0] <= 600 and pygame.mouse.get_pos()[1] >= 200 and pygame.mouse.get_pos()[1] <= 600 and secondScreen == False and previousClick == False and Click[0]:
        secondScreen = True
        mapNumber = random.randint(0,8)
        challengeNumber = random.randint(0,13)

    #Second Screen
    if secondScreen == True:
       
        #Redo Button
        if pygame.mouse.get_pos()[0] >= 690 and pygame.mouse.get_pos()[0] <= 790 and pygame.mouse.get_pos()[1] >= 10 and pygame.mouse.get_pos()[1] <= 60 and previousClick == False and Click[0]:
            mapNumber = random.randint(0,8)
            challengeNumber = random.randint(0,13)
            cyanTimer = 3
            check = False
        if cyanTimer > 0:
            pygame.draw.rect(window, (50,50,50), (690,10,100,50))
            cyanTimer = cyanTimer - 1
        else:
            pygame.draw.rect(window, (80,80,80),(690,10,100,50))
        pygame.draw.rect(window, (30,30,30), (690,10,100,50),5)
        redo = Type2.render("redo",True, (0,0,0))
        window.blit(redo, (703,18))
        
        #Challenge Rule Boxes
        rectdraw2 = 8
        while rectdraw2 > 0:
            pygame.draw.rect(window, (30,30,30), (10,50 + rectdraw2 * 50,35,35),5)
            rectdraw2 = rectdraw2 - 1
        for index, amount in enumerate(bDescriptions):
            bDRender = Type2.render(amount,True,(0,0,0))
            window.blit(bDRender, (50,100 + index * 50))
        pygame.draw.line(window, (0,0,0),(0,90),(360,90),5)
        pygame.draw.line(window, (0,0,0),(0,494),(360,494),5)

        #Excluding challenges on certain maps  
        while check == False:
            if challengeNumber == 4 and mapNumber != 4 and mapNumber != 8:
                mapNumber = random.randint(0,8)
                challengeNumber = random.randint(0,13)
                continue
            if mapNumber == 3 and challengeNumber == 1 or challengeNumber == 2 or challengeNumber == 5 or challengeNumber == 6 or challengeNumber == 11:
                mapNumber = random.randint(0,8)
                challengeNumber = random.randint(0,13)
                continue
            if mapNumber == 2 and challengeNumber == 5 or challengeNumber == 6 or challengeNumber == 11:
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
        mapName = Type2.render(str(Map[mapNumber]), True, (0,0,0))
        challengeName = Type2.render(str(Challenge[challengeNumber]),True, (0,0,0))
        window.blit(mapName, (10,10))
        window.blit(challengeName, (10,50))

        #Fps Counter
        fPS = Type3.render(str(math.trunc(clock.get_fps())) + " fps", True, (0,0,0))
        window.blit(fPS, (755,780))
    
        # Extra info on hover
        if pygame.mouse.get_pos()[0] < 435 and pygame.mouse.get_pos()[1] > 105 and pygame.mouse.get_pos()[1] < 505:
            for x, y in rangesList:
                if int(x) <= pygame.mouse.get_pos()[1] < int(y):
                    displayExtraInfo = index
            PygameCTBF.cursorTextBox((extraInfo.extraInfoDesc[displayExtraInfo]),Type3,(0,0,0),200,window,15,(190,190,190))

    previousClick = Click[0]
    pygame.display.flip()
    clock.tick(30)
pygame.quit()