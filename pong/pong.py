import pygame
import sys

pygame.init()

screenSIZE = screenW , screenH = 1400,1000
gameON = True
screen  = pygame.display.set_mode(screenSIZE)
P1y = 500
P2y = 500
P1down = False
P1up = False
P2down = False
P2up = False
P1speedDOWN = 0.2
P1speedUP   = 0.2
P2speedDOWN = 0.2
P2speedUP   = 0.2
Bally = 550
Ballx = 700
ballLEFT = True
ballRIGHT = False
BallSpeed = 0.2

ballUP = False
ballDOWN = False
Hitspeed = 0
font = pygame.font.Font(None, 72)
p1score = 0
p2score = 0
s1 = pygame.mixer.Sound("pong.wav")
s1.set_volume(0.3)
s2 = pygame.mixer.Sound("pong2.wav")
s2.set_volume(0.3)
text3 = font.render("You win press TAB to play again",True,pygame.Color("white"))
text4 = font.render("You lose press TAB to play again",True,pygame.Color("white"))
Clock = pygame.time.Clock()
winner = None
while True :
    
    while gameON == True :

            
            screen.fill(pygame.Color("black"))

            pygame.draw.rect(screen,pygame.Color("white"),(100,P1y,15,70))
            pygame.draw.rect(screen,pygame.Color("white"),(1280,P2y,15,70))
            pygame.draw.rect(screen,pygame.Color("white"),(700,0,6,1500))

            text1 = font.render(str(p1score),True,pygame.Color("white"))
            text2 = font.render(str(p2score),True,pygame.Color("white"))
            
            screen.blit(text1,(660,10))
            screen.blit(text2,(720,10))
            
            pygame.draw.circle(screen,pygame.Color("white"),(int(Ballx),int(Bally)),(10))  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_UP:
                        P1up = True
                        
                    if event.key == pygame.K_DOWN:
                        P1down = True

                if event.type == pygame.KEYUP:
                    
                    if event.key == pygame.K_UP:
                        P1up = False
                        
                    if event.key == pygame.K_DOWN:
                        P1down = False
                

            if p1score == 6 :

                winner = text3
                Ballx = 700
                Bally = 550
                BallSpeed = 0.2
                ballLEFT = False
                ballRIGHT = True
                ballUP = False
                ballDOWN = False
                gameON = False
                
            if p2score == 6 :

                winner = text4  
                Ballx = 700
                Bally = 550
                BallSpeed = 0.2
                ballLEFT = False
                ballRIGHT = True
                ballUP = False
                ballDOWN = False
                gameON = False 



                
            if P2y + 35 < int(Bally):
                P2down = True
                P2up = False

            if P2y + 35 > int(Bally):
                
                P2up = True
                P2down = False

            



            if ballLEFT == True:
                Ballx -= BallSpeed
                
            if ballRIGHT == True:
                Ballx += BallSpeed

            
            if Bally - 10 < 0 :
                ballDOWN = True
                ballUP = False
                
            if Bally + 10 > 1000 :
                ballUP = True
                ballDOWN = False
                
            if ballDOWN == True:
                Bally += Hitspeed

            
            if ballUP == True:
                Bally -= Hitspeed

            if int(Ballx) < -20:
                s2.play()
                p2score += 1
                Ballx = 700
                Bally = 550
                BallSpeed = 0.2
                ballLEFT = False
                ballRIGHT = True
                ballUP = False
                ballDOWN = False

            if int(Ballx) > 1420:
                s2.play()
                p1score += 1
                Ballx = 700
                Bally =550 
                BallSpeed = 0.2
                ballLEFT = True
                ballRIGHT = False
                ballUP = False
                ballDOWN = False
                
            if int(Ballx) == 115 and P1y < int(Bally) and P1y + 70 > int(Bally):

                s1.play()
                ballLEFT = False
                ballRIGHT = True

                if P1speedUP > 0.2:
                    Hitspeed = P1speedUP
                    ballUP = True
                    ballDOWN = False

                if P1speedDOWN > 0.2:
                    Hitspeed = P1speedDOWN
                    ballDOWN = True
                    ballUP = False

                    
                if BallSpeed < 1:
                    BallSpeed += 0.2

                if P1speedDOWN > 0.2:
                    ballDOWN = True
                    
            if int(Ballx) == 1280 and P2y < int(Bally) and P2y + 70 > int(Bally):

                s1.play()
                ballLEFT = True
                ballRIGHT = False
                
                if BallSpeed < 1:
                    BallSpeed += 0.2





            
            if P1up == True and P1down == False and int(P1y) > 0 :
                P1y -= P1speedUP
                P1speedUP += 0.0045
                
            if P1up == False:
                P1speedUP = 0.2
                
            if P1up == False and P1down == True and int(P1y) < 930:
                P1y += P1speedDOWN
                P1speedDOWN += 0.0045
                
            if P1down == False:
                P1speedDOWN = 0.2


            if P2up == True and P2down == False and int(P2y) > 0 :
                P2y -= P2speedUP
                P2speedUP += 0.0045
                
            if P2up == False:
                P2speedUP = 0.2
                
            if P2up == False and P2down == True and int(P2y) < 930:
                P2y += P2speedDOWN
                P2speedDOWN += 0.0045
                
            if P2down == False:
                P2speedDOWN = 0.2

            Clock.tick(600)
                
            pygame.display.flip()
            
    while gameON == False:
        
        screen.fill(pygame.Color("black"))
        screen.blit(winner,(330,500)) 
        P1y = 500
        P2y = 500
        p1score = 0
        p2score = 0
        P1up = False
        P1down = False
        for event in pygame.event.get():
        
                
            if event.type == pygame.KEYDOWN:
                
                                            
                if event.key == pygame.K_TAB:
                    

                    gameON = True
                    
            pygame.display.flip()


